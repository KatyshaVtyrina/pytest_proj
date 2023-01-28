import pytest

from utils import arrs


@pytest.fixture
def coll():
    return [1, 2, 3, 4]


def test_get_positive(coll):
    assert arrs.get(coll, 1, "test") == 2


def test_get_negative(coll):
    assert arrs.get(coll, -1, "test") == "test"


def test_get_zero(coll):
    assert arrs.get(coll, 0, "test") == 1


def test_slice_positive_start(coll):
    assert arrs.my_slice(coll, 1, 3) == [2, 3]
    assert arrs.my_slice(coll, 1) == [2, 3, 4]


def test_slice_negative_start(coll):
    assert arrs.my_slice(coll, -2) == [3, 4]
    assert arrs.my_slice(coll, -5) == [1, 2, 3, 4]


def test_slice_empty_list():
    assert arrs.my_slice([]) == []
