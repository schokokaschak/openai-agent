import os

# Maximum number of characters the agent's "read file" function can read
MAX_CHARS = 10000

# The working directory where the agent is allowed to:
# - read files
# - write files
# - execute Python files
# - delete files and folders
# Using os.path.abspath ensures we have an absolute path
WORK_DIR = os.path.abspath("./data")

# Instructions for the agent — this tells it what it is allowed to do
# and what tools it can use.
system_prompt = (
    "You are a helpful assistant that can read, write, and execute files. "
    "You have access to tools like get_file_content, get_files_info, write_file, "
    "run_python_file, delete_folder, and delete_file."
)
