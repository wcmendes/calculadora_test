# calculator/core.py

def add(a, b):
    """Soma dois números"""
    return a + b

def subtract(a, b):
    """Subtrai o segundo número do primeiro"""
    return a - b

def multiply(a, b):
    """Multiplica dois números"""
    return a * b

def divide(a, b):
    """Divide o primeiro número pelo segundo"""
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b