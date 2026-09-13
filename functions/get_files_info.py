import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_abs = os.path.abspath(working_directory)
        target_abs = os.path.normpath(os.path.join(working_abs, directory))
        valid_target_dir = os.path.commonpath([working_abs, target_abs]) == working_abs

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_abs):
            return f'Error: "{directory}" is not a directory'

        if valid_target_dir:
            items = []
            for path in os.listdir(target_abs):
                abs_path = os.path.join(target_abs, path)
                items.append({
                    "name": path,
                    "file_size": os.path.getsize(abs_path),
                    "is_dir": os.path.isdir(abs_path)
                })

            result = ""
            for item in items:
                result += f"- {item["name"]}: file_size={item["file_size"]} bytes, is_dir={item["is_dir"]}\n"

            return result
    except Exception:
        return "Error: could not get files info"
