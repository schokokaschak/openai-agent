import os

# how many chars your read function can read
MAX_CHARS = 10000
# the directory where the agent can read/write/execute python files and also DELETE! the files and dirs
WORK_DIR = os.path.abspath("./data")
# this provide your agent what he should know
system_prompt = (
    "You are a helpful assistant that can read, write, and execute files. "
    "You have access to tools like get_file_content, get_files_info, write_file,"
    "run_python_file, delete_folder, and delete_file."
)
