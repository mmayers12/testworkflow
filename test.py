import pytest

def test_success():
    with open('submit.txt') as fin:
        d = fin.read()

    assert d == ''
