# import here
import pytest
from exercises.lists import add_one, get_sum, get_last, all_truthy, reverse_list, biggest_number, insert_at_zero


# @pytest.mark.skip("comment out to run test")
def test_add_one():
    actual = add_one([1,2,3,4,5])
    expected = [2,3,4,5,6]
    assert actual == expected


# @pytest.mark.skip("comment out to run test")
def test_get_sum():
    actual = get_sum([10,15,20,25])
    expected = 70
    assert actual == expected


# @pytest.mark.skip("comment out to run test")
def test_get_last():
    actual = get_last(['a', 'b', 'c'])
    expected = 'c'
    assert actual == expected


# @pytest.mark.skip("comment out to run test")
def test_all_truthy():
    actual = all_truthy(['stuff', True, 1]) # don't make lists with mixed data types!
    expected = True
    assert actual == expected


# @pytest.mark.skip("comment out to run test")
def test_reverse_list():
    actual = reverse_list(['a', 'b', 'c'])
    expected = ['c', 'b', 'a']
    assert actual == expected


# @pytest.mark.skip("comment out to run test")
def test_biggest_number():
    actual = biggest_number([0, -100, 25, 42])
    expected = 42
    assert actual == expected


# @pytest.mark.skip("comment out to run test")
def test_insert_at_zero():
    actual = insert_at_zero(['second', 'third', 'fourth'], 'first')
    expected = ['first', 'second', 'third', 'fourth']
    assert actual == expected
