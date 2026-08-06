import pytest
from password_generator import generate_password

def test_default_length():
    pwd = generate_password()
    assert len(pwd) == 16
    assert any(c.islower() for c in pwd)
    assert any(c.isupper() for c in pwd)
    assert any(c.isdigit() for c in pwd)

def test_custom_length():
    pwd = generate_password(32)
    assert len(pwd) == 32

def test_no_symbols():
    pwd = generate_password(12, use_symbols=False)
    assert all(c.isalnum() for c in pwd)

def test_too_short():
    with pytest.raises(ValueError):
        generate_password(4)