from syntax_checker import SyntaxChecker
import sys
import os
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
bp = Blueprint('syntax_check', __name__)


@bp.route('/syntax-check', methods=('POST',))
def index():
    code = request.form['code']
    language = request.form['language']
    syntax_checker = SyntaxChecker()
    if language == 'python':
        is_valid = syntax_checker.check_python_syntax(code)
    elif language == 'javascript':
        is_valid = syntax_checker.check_javascript_syntax(code)
    elif language == 'java':
        is_valid = syntax_checker.check_java_syntax(code)
    elif language == 'c':
        is_valid = syntax_checker.check_c_syntax(code)
    elif language == 'cpp':
        is_valid = syntax_checker.check_cpp_syntax(code)
    else:
        is_valid = False
    # return render_template('syntax_check/index.html', is_valid=is_valid)
    print("response:", is_valid)
    return {'is_valid': is_valid}
