import os
import tempfile
import subprocess


class SyntaxChecker():

    def check_python_syntax(self, code):
        try:
            process = subprocess.run(['python3', '-c', code], timeout=5)
            return process.returncode == 0
        except subprocess.TimeoutExpired:
            return False

    def check_javascript_syntax(self, code):
        try:
            with open('temp.js', 'w') as f:
                f.write(code)
            process = subprocess.run(['node', '-c', 'temp.js'], timeout=5)
            return process.returncode == 0
        except subprocess.TimeoutExpired:
            return False
        finally:
            os.remove('temp.js')

    def check_java_syntax(self, code):
        # temp = tempfile.NamedTemporaryFile(suffix='.java')
        java_file_name = 'java_code.java'
        try:
            with open(java_file_name, 'w') as f:
                f.write(code)
            process = subprocess.run(['javac', java_file_name], timeout=5)
            return process.returncode == 0
        except subprocess.TimeoutExpired:
            return False
        finally:
            os.remove(java_file_name)

    def check_c_syntax(self, code):
        temp = tempfile.NamedTemporaryFile(suffix='.c', delete=False)
        try:
            with open(temp.name, 'w') as f:
                f.write(code)
            process = subprocess.run(
                ['gcc', '-fsyntax-only', temp.name], timeout=5)
            return process.returncode == 0
        except subprocess.TimeoutExpired:
            return False
        finally:
            os.unlink(temp.name)

    def check_cpp_syntax(self, code):
        temp = tempfile.NamedTemporaryFile(suffix='.cpp', delete=False)
        try:
            with open(temp.name, 'w') as f:
                f.write(code)
            process = subprocess.run(
                ['g++', '-fsyntax-only', temp.name], timeout=5)
            return process.returncode == 0
        except subprocess.TimeoutExpired:
            return False
        finally:
            os.unlink(temp.name)
