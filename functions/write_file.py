import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_abs = os.path.abspath(working_directory)
        target_abs = os.path.normpath(os.path.join(working_abs, file_path))
        valid_target_path = os.path.commonpath([working_abs, target_abs]) == working_abs

        if not valid_target_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_abs):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(target_abs), exist_ok=True)

        with open(target_abs, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception:
        return "Error: could not write content to the file"
