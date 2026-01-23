# integrator/parser.py

from sympy import symbols, expand
from sympy.parsing.sympy_parser import parse_expr
from latex2sympy2 import latex2sympy


def parse_input(expr_input, input_type='string', var_name='x'):
    """
    Парсит входное выражение в зависимости от типа.

    Параметры:
        expr_input (str): входная строка
        input_type (str): 'string' или 'latex'
        var_name (str): имя переменной (например, 'x')

    Возвращает:
        tuple: (выражение SymPy, переменная SymPy)
    """
    var = symbols(var_name)

    if input_type == 'latex':
        # Преобразуем LaTeX → SymPy
        expr = latex2sympy(expr_input)
    else:
        # Преобразуем строку Python → SymPy
        expr = parse_expr(expr_input, evaluate=True)

    # Упрощаем выражение
    expr = expand(expr)

    return expr, var