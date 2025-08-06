import os

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