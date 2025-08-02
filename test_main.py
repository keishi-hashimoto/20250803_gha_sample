from hello import main, double
import pytest


def test__main():
    assert main() == "hello world"


@pytest.mark.parametrize(
    argnames=["val", "expected"],
    argvalues=[
        pytest.param(1, 2, id="returned double value of input"),
        pytest.param(0, 0, id="returned 0 if 0 is given"),
    ],
)
def test_double(val: int, expected: int):
    assert double(val) == expected
