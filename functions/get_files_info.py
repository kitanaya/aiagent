import os


def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_dir = os.path.abspath(directory)
    abs_joined_dir = os.path.join(abs_working_dir, abs_target_dir)
    if directory == None:
        abs_joined_dir = abs_working_dir

    if abs_target_dir.startswith(abs_working_dir):
        pass
    #still poe grinding