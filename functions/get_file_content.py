import os

from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_abs = os.path.abspath(working_directory)
        target_abs = os.path.normpath(os.path.join(working_abs, file_path))
        valid_target_path = os.path.commonpath([working_abs, target_abs]) == working_abs

        if not valid_target_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_abs, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            return file_content_string
    except Exception:
        return "Error: could not get file content"
