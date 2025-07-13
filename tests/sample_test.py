import pytest

def test_simple():
    assert 3 + 2 == 5

def test_one():
    x = "this"
    assert "h" in x

def test_always_fails(record_property):
    # This will always fail
    assert False, "This test is designed to always fail"

@pytest.mark.skip(reason="Skipping this test for demonstration")
def test_skipped_test(record_property):
    # This code won't be executed due to skip decorator
    assert True

@pytest.mark.skipif(True, reason="Conditionally skipped test")
def test_conditionally_skipped(record_property):
    """A test that is conditionally skipped."""
    # This won't run because condition is True
    assert True

def test_skip_test_runtime(record_property):
    # Skip during test execution
    pytest.skip("Skipping this test at runtime")
    # This won't be reached
    assert True
