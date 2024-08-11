import pytest
import plates

def test_mid_num():
    assert plates.is_valid('KKK2KZ') == False
    assert plates.is_valid('Y2K') == False
    assert plates.is_valid('free2m') == False