from solutions.functions import hello, hello_there, knock_knock
import pytest


@pytest.mark.skip("comment out to enable test")
def test_hello():
    actual = hello()
    expected = "Hello"
    assert actual == expected


@pytest.mark.skip("comment out to enable test")
def test_hello_there_positional_argument():
    actual = hello_there("Zelda")
    expected = "Hello, Zelda"
    assert actual == expected


@pytest.mark.skip("comment out to enable test")
def test_hello_there_default_argument():
    actual = hello_there()
    expected = "Hello, stranger"
    assert actual == expected


@pytest.mark.skip("comment out to enable test")
def test_hello_there_multiple_positional_arguments():
    actual = hello_there("Strange","Dr.")
    expected = "Hello, Dr. Strange"
    assert actual == expected

@pytest.mark.skip("comment out to enable test")
def test_hello_there_key_word_arguments():
    actual = hello_there(prefix="Madame",subject="Futzinderdoor")
    expected = "Hello, Madame Futzinderdoor"
    assert actual == expected


@pytest.mark.skip("comment out to enable test")
def test_knock_knock():
    actual = knock_knock(long="no panth, I'm going thwimming!",short="Panther")

    expected = """knock knock.
Who's there?
Panther.
Panther who?
Panther no panth, I'm going thwimming!"""
    
    assert actual == expected