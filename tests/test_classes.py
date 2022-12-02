import pytest
from exercises.classes import Dog, Mammal, Cat, Sphynx


@pytest.mark.skip("comment out to enable test")
def test_stray_dog():
    pooch = Dog()
    actual = pooch.name
    expected = "unknown"
    assert actual == expected


@pytest.mark.skip("comment out to enable test")
def test_named_dog():
    pooch = Dog("Rex")
    actual = pooch.name
    expected = "Rex"
    assert actual == expected


@pytest.mark.skip("comment out to enable test")
def test_dog_is_mammal():
    pooch = Dog("Rex")
    actual = isinstance(pooch, Mammal)
    expected = True
    assert actual == expected


@pytest.mark.skip("comment out to enable test")
def test_dog_has_hair():
    pooch = Dog("Rex")
    actual = pooch.has_hair
    expected = True
    assert actual == expected


@pytest.mark.skip("comment out to enable test")
def test_hairless_sphynx():
    kitty = Sphynx()
    actual = kitty.has_hair
    expected = False
    assert actual == expected
