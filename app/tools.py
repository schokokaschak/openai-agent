from agents import function_tool
import os
import subprocess
import shutil
from app.config import WORK_DIR, MAX_CHARS


@function_tool
def get_file_content(file_path: str) -> str:
    """
    Reads up to MAX_CHARS characters from a file within the WORK_DIR.
    Returns an error if the file is outside the working directory or cannot be read.
    """
    abs_file_path = os.path.abspath(os.path.join(WORK_DIR, file_path))
    if not abs_file_path.startswith(WORK_DIR):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_file_path, "r") as f:
            content = f.read(MAX_CHARS)
            if os.path.getsize(abs_file_path) > MAX_CHARS:
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'


@function_tool
def get_files_info(directory: str = ".") -> str:
    """
    Lists all files in a directory within WORK_DIR.
    Returns filename, size, and whether it is a directory.
    """
    target_dir = os.path.abspath(os.path.join(WORK_DIR, directory))
    if not target_dir.startswith(WORK_DIR):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"


@function_tool
def write_file(file_path: str, content: str) -> str:
    """
    Writes content to a file within WORK_DIR. Creates directories if needed.
    Returns an error if writing fails or the path is a directory.
    """
    abs_file_path = os.path.abspath(os.path.join(WORK_DIR, file_path))
    if not abs_file_path.startswith(WORK_DIR):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        try:
            os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    if os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
        return f'Error: "{file_path}" is a directory, not a file'
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: writing to file: {e}"


@function_tool
def run_python_file(file_path: str, args: list = None) -> str:
    """
    Executes a Python file within WORK_DIR.
    Optional 'args' can be passed to the Python script.
    Returns stdout, stderr, and exit code.
    """
    abs_file_path = os.path.abspath(os.path.join(WORK_DIR, file_path))
    if not abs_file_path.startswith(WORK_DIR):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        commands = ["python", abs_file_path]
        if args:
            commands.extend(args)
        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=WORK_DIR,
        )
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"


@function_tool
def delete_file(file_path: str) -> str:
    """
    Deletes a file within WORK_DIR.
    Returns an error if the file does not exist or is a directory.
    """
    abs_file_path = os.path.abspath(os.path.join(WORK_DIR, file_path))
    if not abs_file_path.startswith(WORK_DIR):
        return f'Error: Cannot delete "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if os.path.isdir(abs_file_path):
        return f'Error: "{file_path}" is a directory, not a file'
    try:
        os.remove(abs_file_path)
        return f'Successfully deleted "{file_path}"'
    except Exception as e:
        return f"Error: deleting file: {e}"


@function_tool
def delete_folder(folder_path: str) -> str:
    """
    Deletes a folder and all its contents within WORK_DIR.
    Returns an error if the folder does not exist or is not a directory.
    """
    abs_folder_path = os.path.abspath(os.path.join(WORK_DIR, folder_path))
    if not abs_folder_path.startswith(WORK_DIR):
        return f'Error: Cannot delete "{folder_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_folder_path):
        return f'Error: Folder "{folder_path}" not found.'
    if not os.path.isdir(abs_folder_path):
        return f'Error: "{folder_path}" is not a folder'
    try:
        shutil.rmtree(abs_folder_path)
        return f'Successfully deleted folder "{folder_path}" and all its contents'
    except Exception as e:
        return f"Error: deleting folder: {e}"
