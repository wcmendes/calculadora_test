# tests/test_core.py

import pytest
from calculator.core import add, subtract, multiply, divide

def test_add():
    """Testa a função de soma"""
    assert add(2, 3) == 6
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Testa a função de subtração"""
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5

def test_multiply():
    """Testa a função de multiplicação"""
    assert multiply(3, 4) == 12
    assert multiply(-1, 5) == -5

def test_divide():
    """Testa a função de divisão"""
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    """Testa a exceção de divisão por zero"""
    with pytest.raises(ValueError):
        divide(10, 0)