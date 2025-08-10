import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        completed_process = subprocess.run([
            "python", abs_file_path, *args
            ], 
            timeout=30,
            capture_output=True,
            cwd=abs_working_dir     
        )
    except Exception as e:
        return f"Error: executing Python file: {e}"

    stdout_str = completed_process.stdout.decode("utf-8").strip()
    stderr_str = completed_process.stderr.decode("utf-8").strip()
    output_message = ""

    
    if stdout_str:
        output_message = f"STDOUT: {stdout_str}\n"
    if stderr_str:
        output_message += f"STDERR: {stderr_str}\n"
    if completed_process.returncode != 0:
        output_message += f"Process exited with code {completed_process.returncode}"
    if not output_message:
        output_message = "No output produced."
    return output_message


