from unittest import mock
import pytest
from pydir.Functions.Checkout_module import foo

@pytest.fixture
def fixture1():
    def param():
        return {"a":5,"b":4,"c":3,'d':2,"e":1}
    return param
def test_foo(fixture1):
    r = foo(fixture1)
    assert r == 15