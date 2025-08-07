import os
from functions.config import MAX_CHARS


def get_files_info(working_directory, directory="."):
	abs_path = os.path.abspath(os.path.join(working_directory, directory))
	if not abs_path.startswith(os.path.abspath(working_directory)):
		return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
	if not os.path.isdir(abs_path):
		return f'Error: "{directory}" is not a directory'
	
	try:
		items = os.listdir(abs_path)
		formatted_items = []
		for item in items:
			full_item_path = os.path.join(abs_path, item)
			formatted_items.append(f"- {item}: file_size={os.path.getsize(full_item_path)} bytes, is_dir={os.path.isdir(full_item_path)}")
		return "\n".join(formatted_items)
	except Exception as e:
		return f"Error: {str(e)}"
	

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
				return f'{file_content_string}\n[...File "{file_path}" truncated at 10000 characters].'
	except Exception as e:
		return f"Error: {str(e)}"
	 

