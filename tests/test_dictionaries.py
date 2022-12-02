import pytest
from exercises.dictionaries import get_dictionary

@pytest.mark.skip("comment out to enable test")
def test_dictionary():
    actual = get_dictionary()
    expected = {}
    assert actual == expected


@pytest.mark.skip("comment out to enable test")
def test_dictionary_with_key_and_value():
    actual = get_dictionary("my_key", "my_value")
    expected = {"my_key": "my_value"}
    assert actual == expected