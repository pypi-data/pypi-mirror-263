import copy
import dataclasses
import functools
import inspect
from typing import TypeVar, Callable, Type, Any

import rmk2.data.dictionary

T = TypeVar("T")


class Missing:
    pass


def merge(left: T, right: T, merge_lists: bool = False, merge_dicts: bool = False) -> T:
    """Recursively merge two class instances, key by key"""
    assert type(left) is type(
        right
    ), f"Cannot merge different Types, left='{type(left)}', right='{type(right)}'"

    primitives = [int, str, float, bool, list, dict, set, type(None)]
    kwargs = {}

    for k in {*vars(left).keys(), *vars(right).keys()}:
        _left = getattr(left, k, None)
        _right = getattr(right, k, None)

        if (
            type(_left) not in primitives
            and type(_right) not in primitives
            and type(_left) is type(_right)
        ):
            merged = merge(
                left=_left,
                right=_right,
                merge_lists=merge_lists,
                merge_dicts=merge_dicts,
            )
        elif isinstance(_left, list) and isinstance(_right, list) and merge_lists:
            merged = [*_left, *_right]
        elif isinstance(_left, dict) and isinstance(_right, dict) and merge_dicts:
            merged = rmk2.data.dictionary.merge(
                left=_left, right=_right, merge_lists=merge_lists
            )
        elif not _left and _right is not None:
            merged = _right
        else:
            merged = _right or _left

        kwargs[k] = merged

    return type(left)(**kwargs)


def get_path(cls: object, path: list[str] | str, default: Any | None = None) -> Any:
    """Get attribute from an object, nested under a given path"""
    path = path.split(".") if isinstance(path, str) else path
    result = functools.reduce(lambda a, b: getattr(a, b, Missing), path, cls)

    return default if result == Missing else result


def get_metaclass(cls: object) -> Type:
    """Get the root metaclass for a given object"""
    _tree = inspect.getclasstree([cls if isinstance(cls, Type) else type(cls)])

    return _tree[0][0] if _tree else type(None)


def pushdown(func: Callable, parent: list[str] = None) -> Callable:
    """Recursively apply a class method to all subclasses of a given class"""
    parent = parent or []

    @functools.wraps(func)
    def wrapper(cls: T, *args, **kwargs) -> T:
        _fields = {
            f.name
            for f in dataclasses.fields(cls)
            if dataclasses.is_dataclass(f.type)
            and issubclass(f.type, get_metaclass(cls))
        }

        for k in _fields:
            # Affect current subclass
            func(getattr(cls, k), *args, **kwargs)

            # Recurse further for nodes underneath current subclass
            pushdown(func, parent=[*parent, k])(getattr(cls, k), *args, **kwargs)

        return cls

    return wrapper
