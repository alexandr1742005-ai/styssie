from flask import Flask, render_template, request, jsonify
from sympy import symbols, integrate, latex
from sympy.parsing.sympy_parser import parse_expr

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

from integrator.parser import parse_input
from integrator.step_solver import solve_integral_step_by_step_from_expr

@app.route('/solve', methods=['POST'])
def solve_string():
    data = request.get_json()
    expr_str = data.get('expression', 'x**2')
    try:
        expr, var = parse_input(expr_str, input_type='string')
        steps = solve_integral_step_by_step_from_expr(expr, var)
        return jsonify({"success": True, "steps": steps})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@app.route('/solve-latex', methods=['POST'])
def solve_latex():
    data = request.get_json()
    latex_str = data.get('latex', '')
    try:
        expr, var = parse_input(latex_str, input_type='latex')
        steps = solve_integral_step_by_step_from_expr(expr, var)
        return jsonify({"success": True, "steps": steps})
    except Exception as e:
        return jsonify({"success": False, "error": f"Не удалось распознать формулу: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(debug=True)
    from flask import Flask, render_template, request, jsonify
    from sympy import symbols, latex as sym_latex
    from latex2sympy2 import latex2sympy  # <-- НОВОЕ

    app = Flask(__name__)


    # ... существующий маршрут / ...

    @app.route('/solve-latex', methods=['POST'])
    def solve_latex():
        data = request.get_json()
        latex_str = data.get('latex', '')

        try:
            # Преобразуем LaTeX → SymPy выражение
            expr = latex2sympy(latex_str)
            var = symbols('x')  # пока фиксируем переменную как x

            # Передаём в наш пошаговый решатель
            from integrator.step_solver import solve_integral_step_by_step_from_expr
            steps = solve_integral_step_by_step_from_expr(expr, var)

            return jsonify({"success": True, "steps": steps})
        except Exception as e:
            return jsonify({"success": False, "error": f"Не удалось распознать формулу: {str(e)}"}), 400