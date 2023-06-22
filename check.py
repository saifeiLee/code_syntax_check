from syntax_checker import SyntaxChecker
import os

checker = SyntaxChecker()


script_dir = os.path.dirname(__file__)


def test_python():
    with open(f"{script_dir}/test/python_code.py", "r") as f:
        python_code = f.read()
        check_result = checker.check_python_syntax(python_code)
        print("------ check python code ------")
        print(check_result)


def test_js():
    with open(f"{script_dir}/test/js_code.js", "r") as f:
        js_code = f.read()
        check_result = checker.check_javascript_syntax(js_code)
        print("------ check js code ------")
        print(check_result)


def check_java():
    with open(f"{script_dir}/test/java_code.java", "r") as f:
        java_code = f.read()
        check_result = checker.check_java_syntax(java_code)
        print("------ check java code ------")
        print(check_result)


def check_c():
    with open(f"{script_dir}/test/c_code.c", "r") as f:
        c_code = f.read()
        check_result = checker.check_c_syntax(c_code)
        print("------ check c code ------")
        print(check_result)


def check_cpp():
    with open(f"{script_dir}/test/cpp_code.cpp", "r") as f:
        cpp_code = f.read()
        check_result = checker.check_cpp_syntax(cpp_code)
        print("------ check cpp code ------")
        print(check_result)


if __name__ == '__main__':
    for i in range(3):
        test_python()
        test_js()
        check_java()
        check_c()
        check_cpp()
