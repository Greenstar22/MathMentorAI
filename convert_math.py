import json
import re

def convert_to_asciimath(expr):
    if not isinstance(expr, str):
        return expr

    # Normalize whitespace and symbols
    expr = expr.replace('−', '-').replace('×', '*').replace('÷', '/')
    expr = expr.replace('\\/', '/').replace('=', '=')

    # Convert LaTeX-style fractions: \frac{a}{b} → a/b
    expr = re.sub(r'\\frac\s*\{([^{}]+)\}\s*\{([^{}]+)\}', r'(\1)/(\2)', expr)

    # Convert LaTeX-style square roots: \sqrt{a} → sqrt(a)
    expr = re.sub(r'\\sqrt\s*\{([^{}]+)\}', r'sqrt(\1)', expr)

    # Convert exponents: x^{2} → x^2
    expr = re.sub(r'([a-zA-Z0-9]+)\s*\^\s*\{([^{}]+)\}', r'\1^\2', expr)
    expr = re.sub(r'([a-zA-Z0-9]+)\s*\^\s*([a-zA-Z0-9]+)', r'\1^\2', expr)

    # Convert mixed numbers: 3 1/2 → 3+1/2
    expr = re.sub(r'(\d+)\s+(\d+)/(\d+)', r'\1+(\2/\3)', expr)

    # Convert Greek letters: \alpha → alpha
    greek_map = {
        'alpha': 'alpha', 'beta': 'beta', 'gamma': 'gamma', 'delta': 'delta',
        'epsilon': 'epsilon', 'theta': 'theta', 'lambda': 'lambda',
        'mu': 'mu', 'pi': 'pi', 'sigma': 'sigma', 'phi': 'phi', 'omega': 'omega'
    }
    for latex, ascii in greek_map.items():
        expr = expr.replace(f'\\{latex}', ascii)

    # Remove unnecessary LaTeX formatting
    expr = expr.replace('\\left', '').replace('\\right', '')
    expr = expr.replace('{', '(').replace('}', ')')

    return expr.strip()

def process_json(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for entry in data:
        for key in ['Incorrect Answer', 'Correct Answer']:
            if key in entry:
                original = entry[key]
                entry[key] = convert_to_asciimath(original)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

# Example usage
process_json('data.json', 'data_asciimath.json')