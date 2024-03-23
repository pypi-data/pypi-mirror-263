import dataclasses
from typing import Any

import pytest

import rmk2.data.object
from tests.conftest import Default


class Mock:
    def __init__(self, /, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self) -> dict:
        """Recursively dump all values to a (potentially nested) dictionary"""
        return {
            k: v.to_dict() if isinstance(v, type(self)) else v
            for k, v in vars(self).items()
        }


def test_mock_to_dict() -> None:
    """Check Mock class dictionary dumping, which is needed for test comparisons"""
    source = Mock(a=1, b=Mock(c=3, d=Mock(e=5, f=Mock(g=7))))

    parsed = source.to_dict()
    expected = {"a": 1, "b": {"c": 3, "d": {"e": 5, "f": {"g": 7}}}}

    assert isinstance(parsed, dict)
    assert parsed == expected


@pytest.mark.parametrize(
    "left,right,expected,merge_lists,merge_dicts",
    [
        (Mock(), Mock(), Mock(), False, False),  # empty
        (Mock(a=1), Mock(), Mock(a=1), False, False),  # keep left
        (Mock(), Mock(a=1), Mock(a=1), False, False),  # keep right
        (Mock(a=1), Mock(a=2), Mock(a=2), False, False),  # overwrite
        (Mock(a=1), Mock(b=2), Mock(a=1, b=2), False, False),  # difference
        (
            Mock(a=1, b=Mock(c=3)),
            Mock(b=Mock(c=-3)),
            Mock(a=1, b=Mock(c=-3)),
            False,
            False,
        ),  # nested overwrite
        (
            Mock(a=1, b=Mock(c=3)),
            Mock(b=Mock(d=4)),
            Mock(a=1, b=Mock(c=3, d=4)),
            False,
            False,
        ),  # nested difference
        (Mock(a=[1]), Mock(a=[2]), Mock(a=[2]), False, False),  # list overwrite
        (Mock(a=[1]), Mock(a=[2]), Mock(a=[1, 2]), True, False),  # list merge
        (
            Mock(a={"x": 1}),
            Mock(a={"y": 2}),
            Mock(a={"y": 2}),
            False,
            False,
        ),  # dict overwrite
        (
            Mock(a={"x": 1}),
            Mock(a={"y": 2}),
            Mock(a={"x": 1, "y": 2}),
            False,
            True,
        ),  # dict merge
        (Mock(a=None), Mock(a=True), Mock(a=True), False, False),  # truthy overwrite
        (Mock(a=None), Mock(a=False), Mock(a=False), False, False),  # falsy overwrite
        (Mock(a=None), Mock(a=None), Mock(a=None), False, False),  # keep null
    ],
)
def test_merge(left, right, expected, merge_lists, merge_dicts):
    """Check merging two objects into a single object"""
    merged = rmk2.data.object.merge(
        left=left, right=right, merge_lists=merge_lists, merge_dicts=merge_dicts
    )

    assert isinstance(merged, type(left))
    assert isinstance(merged, type(right))

    assert merged.to_dict() == expected.to_dict()


def test_merge_exception():
    """Check exception when trying to merge differently typed objects"""

    class Left:
        pass

    class Right:
        pass

    with pytest.raises(AssertionError) as e:
        rmk2.data.object.merge(left=Left(), right=Right())

    assert str(e.value).startswith("Cannot merge different Types")


@pytest.mark.parametrize(
    "cls,path,default,expected",
    [
        (Mock(a=1), ["a"], Default, 1),  # non-nested, list path
        (Mock(a=1), "a", Default, 1),  # non-nested, string path
        (Mock(a=Mock(b=3)), ["a", "b"], Default, 3),  # nested, list path
        (Mock(a=Mock(b=3)), "a.b", Default, 3),  # nested, string path
        (Mock(), ["missing"], Default, Default),  # missing value
        (Mock(a=Mock(b=3)), ["a.missing"], Default, Default),  # missing nested value
        (Mock(a=Mock(b=None)), "a.b", Default, None),  # existing null value
        (Mock(a=Mock(b=False)), "a.b", Default, False),  # existing falsy value
    ],
)
def test_get_path(cls, path, default, expected) -> None:
    """Check getting values via path from objects"""
    parsed = rmk2.data.object.get_path(cls=cls, path=path, default=default)

    assert parsed == expected


def test_get_metaclass() -> None:
    """Check getting the root metaclass for a given object"""

    class Foo:
        pass

    class Bar(Foo):
        pass

    class Baz(Foo):
        pass

    class Bat(Bar):
        pass

    _types = [(Foo, object), (Bar, Foo), (Baz, Foo), (Bat, Bar)]

    for _type, _expected in _types:
        # Check raw type
        assert rmk2.data.object.get_metaclass(cls=_type) is _expected

        # Check instance
        assert rmk2.data.object.get_metaclass(cls=_type()) is _expected


def test_pushdown() -> None:
    """Check recursive application of class methods for subclasses"""

    @dataclasses.dataclass
    class Main:
        @rmk2.data.object.pushdown
        def set_x(self, value: Any) -> None:
            setattr(self, "x", value)

    @dataclasses.dataclass
    class Child(Main):
        pass

    @dataclasses.dataclass
    class TestClass(Main):
        a: Child = dataclasses.field(default_factory=Child)
        b: Child = dataclasses.field(default_factory=Child)
        c: Child = dataclasses.field(default_factory=Child)

    initialised = TestClass()

    # Check that attribute "x" does not yet exist
    for k in ["a", "b", "c"]:
        assert not hasattr(getattr(initialised, k), "x")

    # Check that x gets set for all subclasses/children
    _value = 42
    initialised.set_x(value=_value)

    for k in map(lambda x: x.name, dataclasses.fields(TestClass)):
        assert hasattr(getattr(initialised, k), "x")
        assert getattr(getattr(initialised, k), "x") == _value
