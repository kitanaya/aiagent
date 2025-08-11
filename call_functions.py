from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_files_content import schema_get_files_content
from functions.run_python_file import schema_run_python_file


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_files_content,
        schema_run_python_file,
    ]
)