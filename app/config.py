import os
# how many chars your read function can read
MAX_CHARS = 10000
# the directory where the agent can read/write/execute python files and also DELETE! the files and dirs
WORK_DIR = os.path.abspath("./evals")