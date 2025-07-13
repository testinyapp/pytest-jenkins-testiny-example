import pytest

def test_another_simple(record_property):
    record_property("type", "smoke")
    assert 3 + 2 == 5
