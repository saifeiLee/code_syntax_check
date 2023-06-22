import os
import tempfile
import subprocess


class SyntaxChecker():

    def check_python_syntax(self, code):
        try:
            process = subprocess.run(
                ['python3', '-c', code], stderr=subprocess.PIPE, timeout=5)
            if process.returncode == 0:
                return True, "Success"
            else:
                return False, process.stderr.decode('utf-8')
        except subprocess.TimeoutExpired:
            return False, "Timeout expired"

    def check_javascript_syntax(self, code):
        try:
            with open('temp.js', 'w') as f:
                f.write(code)
            process = subprocess.run(
                ['node', '-c', 'temp.js'], stderr=subprocess.PIPE, timeout=5)
            if process.returncode == 0:
                return True, "Success"
            else:
                return False, process.stderr.decode('utf-8')
        except subprocess.TimeoutExpired:
            return False, "Timeout expired"
        finally:
            os.remove('temp.js')

    def check_java_syntax(self, code):
        temp = tempfile.NamedTemporaryFile(suffix='.java', delete=False)
        # java_file_name = 'java_code.java'
        java_file_name = temp.name
        try:
            with open(java_file_name, 'w') as f:
                f.write(code)
            process = subprocess.run(
                ['javac', java_file_name], stderr=subprocess.PIPE, timeout=5)
            if process.returncode == 0:
                return True, "Success"
            else:
                return False, process.stderr.decode('utf-8')
        except subprocess.TimeoutExpired:
            return False, "Timeout expired"
        finally:
            os.remove(java_file_name)

    def check_c_syntax(self, code):
        temp = tempfile.NamedTemporaryFile(suffix='.c', delete=False)
        try:
            with open(temp.name, 'w') as f:
                f.write(code)
            process = subprocess.run(
                ['gcc', '-fsyntax-only', temp.name], stderr=subprocess.PIPE, timeout=5)
            if process.returncode == 0:
                return True, "Success"
            else:
                return False, process.stderr.decode('utf-8')
        except subprocess.TimeoutExpired:
            return False, "Timeout expired"
        finally:
            os.unlink(temp.name)

    def check_cpp_syntax(self, code):
        temp = tempfile.NamedTemporaryFile(suffix='.cpp', delete=False)
        try:
            with open(temp.name, 'w') as f:
                f.write(code)
            process = subprocess.run(
                ['g++', '-fsyntax-only', temp.name], stderr=subprocess.PIPE, timeout=5)
            if process.returncode == 0:
                return True, "Success"
            else:
                return False, process.stderr.decode('utf-8')
        except subprocess.TimeoutExpired:
            return False, "Timeout expired"
        finally:
            os.unlink(temp.name)
