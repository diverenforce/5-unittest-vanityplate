import pytest
import plates

def test_mid_num():
    assert plates.is_valid('KKK2KZ') == False
    assert plates.is_valid('Y2K') == False
    assert plates.is_valid('free2m') == False

def test_less():
    assert plates.is_valid('2') == False
    assert plates.is_valid('a') == False

def test_more():
    assert plates.is_valid('NOOOOOOOOOOOOOOOOOOO!!!!!') == False
    assert plates.is_valid('298746589ladfa98374') == False

def test_first():
    assert plates.is_valid('2y') == False
    assert plates.is_valid('21') == False
    assert plates.is_valid('ka') == True
    assert plates.is_valid('tw') == True

def test_punct():
    assert plates.is_valid('p!!hah') == False
    assert plates.is_valid('!@#$') == False
    assert plates.is_valid('no!!1') ==  False