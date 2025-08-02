from hello import main, double


def test__main():
    assert main() == "hello world"


def test_double():
    assert double(2) == 4
