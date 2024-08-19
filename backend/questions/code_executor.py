import subprocess
import tempfile
import os

def execute_python_code(code, test_cases):
    results = []
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
        temp_file.write(code)
        temp_file_path = temp_file.name

    try:
        for test_case in test_cases:
            process = subprocess.Popen(['python', temp_file_path],
                                       stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       text=True)
            stdout, stderr = process.communicate(input=test_case.get('input', ''))
            
            results.append({
                'passed': stdout.strip() == test_case.get('expected_output', '').strip(),
                'output': stdout,
                'error': stderr
            })
    finally:
        os.unlink(temp_file_path)

    return results