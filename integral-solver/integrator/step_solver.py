from sympy import symbols, latex as sym_latex, integrate
from .rules.polynomial import integrate_polynomial


def solve_integral_step_by_step_from_expr(expr, var):
    """
    Генерирует пошаговое решение интеграла на основе уже разобранного выражения SymPy.

    Параметры:
        expr (sympy.Expr): выражение для интегрирования (например, 3*x**2 + 2*x)
        var (sympy.Symbol): переменная интегрирования (например, x)

    Возвращает:
        list[dict]: список шагов вида {"explanation": "...", "math": "..." }
    """
    steps = []

    # Шаг 0: Показываем исходный интеграл
    steps.append({
        "explanation": "Рассмотрим интеграл:",
        "math": f"\\int {sym_latex(expr)} \\, d{var}"
    })

    # Проверяем, является ли выражение полиномом от переменной var
    if expr.is_polynomial(var):
        return integrate_polynomial(expr, var, steps)
    else:
        # Fallback: используем общий метод интегрирования
        try:
            result = integrate(expr, var)
            steps.append({
                "explanation": "Это не полином. Решаем напрямую с помощью символьного интегрирования:",
                "math": f"{sym_latex(result)} + C"
            })
        except Exception as e:
            steps.append({
                "explanation": "Не удалось найти аналитический интеграл.",
                "math": "\\text{Интеграл не выражается в элементарных функциях.}"
            })
        return steps