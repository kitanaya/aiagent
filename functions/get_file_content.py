import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
	abs_working_dir = os.path.abspath(working_directory)
	target_dir = os.path.abspath(os.path.join(working_directory, file_path))
	if not target_dir.startswith(abs_working_dir):
		return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
	if not os.path.isfile(target_dir):
		return f'Error: File not found or is not a regular file: "{file_path}"'
	
	try:
		with open(target_dir, "r") as f:
			file_content_string = f.read(MAX_CHARS)
			if len(file_content_string) < MAX_CHARS:
				return file_content_string
			else:
				return f'{file_content_string}[...File "{file_path}" truncated at {MAX_CHARS} characters]'
	except Exception as e:
		return f'Error reading file "{file_path}": {e}'


schema_get_file_content= types.FunctionDeclaration(
    name="get_file_content",
    description="Lists the content of the specified file with a maximum of 10000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file itself to list the content from, relative to the working directory.",
            ),
        },
    ),
)