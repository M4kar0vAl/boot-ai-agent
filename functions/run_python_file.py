import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_abs = os.path.abspath(working_directory)
        target_abs = os.path.normpath(os.path.join(working_abs, file_path))
        valid_target_path = os.path.commonpath([working_abs, target_abs]) == working_abs

        if not valid_target_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_abs):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_abs]

        if args:
            command.extend(args)

        completed_process = subprocess.run(command, cwd=working_abs, capture_output=True, text=True, timeout=30)
        output_string = ""

        if completed_process.returncode != 0:
            output_string += f"Process exited with code {completed_process.returncode}\n"

        if not (completed_process.stdout or completed_process.stderr):
            output_string += "No output produced\n"
        else:
            output_string += f"STDOUT: {completed_process.stdout}\n"
            output_string += f"STDERR: {completed_process.stderr}\n"

        return output_string
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Run python file relative to the working directory. Executes python file and returns exit code, stdout and stderr",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Python file path to execute, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of arguments to execute python file. Default is empty list.",
                },
            },
            "required": ["file_path"]
        },
    },
}
