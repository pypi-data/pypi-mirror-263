import pytest

import rmk2.data.dictionary
from tests.conftest import Default


@pytest.mark.parametrize(
    "left,right,expected,merge_lists",
    [
        ({}, {}, {}, False),  # empty
        ({"a": 1}, {}, {"a": 1}, False),  # keep left
        ({}, {"a": 1}, {"a": 1}, False),  # keep right
        ({"a": 1}, {"a": 2}, {"a": 2}, False),  # overwrite
        ({"a": 1}, {"b": 2}, {"a": 1, "b": 2}, False),  # difference
        (
            {"a": 1, "b": {"c": 3}},
            {"b": {"c": 4}},
            {"a": 1, "b": {"c": 4}},
            False,
        ),  # nested overwrite
        (
            {"a": 1, "b": {"c": 3}},
            {"b": {"d": 4}},
            {"a": 1, "b": {"c": 3, "d": 4}},
            False,
        ),  # nested difference
        ({"a": [1]}, {"a": [2]}, {"a": [2]}, False),  # list overwrite
        ({"a": [1]}, {"a": [2]}, {"a": [1, 2]}, True),  # list merge
        ({"a": None}, {"a": True}, {"a": True}, False),  # truthy overwrite
        ({"a": None}, {"a": False}, {"a": False}, False),  # falsy overwrite
        ({"a": None}, {"a": None}, {"a": None}, False),  # keep null
    ],
)
def test_merge(left, right, expected, merge_lists) -> None:
    """Check merging two dictionaries into a single dictionary"""
    merged = rmk2.data.dictionary.merge(left=left, right=right, merge_lists=merge_lists)

    assert isinstance(merged, dict)
    assert merged == expected


@pytest.mark.parametrize(
    "data,path,default,expected",
    [
        ({"a": 1}, ["a"], Default, 1),  # non-nested, list path
        ({"a": 1}, "a", Default, 1),  # non-nested, string path
        ({"a": {"b": {"c": 3}}}, ["a", "b", "c"], Default, 3),  # nested, list path
        ({"a": {"b": {"c": 3}}}, "a.b.c", Default, 3),  # nested, string path
        ({}, ["x"], Default, Default),  # missing value
        ({"x": {"z": False}}, ["x.y"], Default, Default),  # missing nested value
        ({"a": {"b": {"c": None}}}, "a.b.c", Default, None),  # existing null value
        ({"a": {"b": {"c": False}}}, "a.b.c", Default, False),  # existing falsy value
    ],
)
def test_get_path(data, path, default, expected) -> None:
    """Check getting values via path from dictionary"""
    parsed = rmk2.data.dictionary.get_path(data=data, path=path, default=default)

    assert parsed == expected


@pytest.mark.parametrize(
    "data,path,value,expected",
    [
        ({}, ["a"], 1, {"a": 1}),  # non-nested, list path
        ({}, "a", 1, {"a": 1}),  # non-nested, string path
        ({}, ["a", "b", "c"], 3, {"a": {"b": {"c": 3}}}),  # nested, list path
        ({}, "a.b.c", 3, {"a": {"b": {"c": 3}}}),  # nested, string path
        ({"a": 1}, ["b"], 2, {"a": 1, "b": 2}),  # additive
        ({"a": 1}, ["a"], 2, {"a": 2}),  # overwrite
        ({"a": {"b": 2}}, "a.b", 3, {"a": {"b": 3}}),  # nested overwrite
        (
            {"a": {"b": 2, "c": 3}},
            "a.b",
            3,
            {"a": {"b": 3, "c": 3}},
        ),  # partial nested overwrite
    ],
)
def test_put_path(data, path, value, expected) -> None:
    """Check inserting values via path into a dictionary"""
    added = rmk2.data.dictionary.put_path(data=data, path=path, value=value)

    assert isinstance(added, dict)
    assert added == expected
