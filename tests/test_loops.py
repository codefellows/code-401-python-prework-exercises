import pytest
from exercises.loops import capitalize_first_letter, sum_of_second_numbers, remove_duplicates


# @pytest.mark.skip("comment out to enable test")
def test_capitalize_first_letter():
    actual = capitalize_first_letter(['washington', 'oregon', 'america'])
    expected = ['Washington', 'Oregon', 'America']
    assert actual == expected


# @pytest.mark.skip("comment out to enable test")
def test_sum_of_second_numbers():
    actual = sum_of_second_numbers([[15, 20], [3, 7], [-2, 16]])
    expected = 43
    assert actual == expected


def test_remove_duplicates():
    actual = remove_duplicates([2, 2, 4, 4, 8, 8])
    expected = [2, 4, 8]
    assert actual == expected