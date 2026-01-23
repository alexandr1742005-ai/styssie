from sympy import symbols, latex, expand
from sympy.core.add import Add
from sympy.core.mul import Mul
from sympy.core.power import Pow
from sympy.core.numbers import Number


def integrate_polynomial(expr, var, steps):
    """
    Генерирует пошаговое решение для полинома.
    expr — выражение SymPy (например, 3*x**2 + 2*x + 5)
    var — переменная интегрирования (например, x)
    steps — список, в который добавляются шаги
    """
    steps.append({
        "explanation": "Интеграл от полинома решается почленным интегрированием.",
        "math": f"\\int {latex(expr)} \\, d{var}"
    })

    # Разбиваем на слагаемые
    terms = expr.as_ordered_terms() if isinstance(expr, Add) else [expr]

    total_result = 0
    term_results = []

    for term in terms:
        # Интегрируем одно слагаемое
        integral_term = term.integrate(var)
        total_result += integral_term

        # Пояснение для каждого слагаемого
        explanation = f"∫ {latex(term)} \\, d{var} = {latex(integral_term)}"
        steps.append({
            "explanation": "",
            "math": explanation
        })
        term_results.append(integral_term)

    # Финальный результат
    final_expr = expand(total_result)  # упрощаем
    steps.append({
        "explanation": "Складываем все полученные интегралы:",
        "math": f"{latex(final_expr)} + C"
    })

    return steps