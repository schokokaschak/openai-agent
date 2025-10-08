# OpenAI Agent Playground

An interactive AI assistant that can read, write, execute, and delete files within a controlled working directory. Includes custom tools and supports automated evaluation using DeepEval.

## Features

- Read file contents (max 10,000 characters)
- List files and directories
- Write to files
- Execute Python scripts
- Delete files or directories
- Testable with DeepEval metrics: Faithfulness, JSON correctness, Answer relevancy, GEval

## Installation & Setup

git clone https://github.com/yourusername/openai-agent-playground.git
cd openai-agent-playground
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# OR on Windows:
# .venv\Scripts\activate
pip install -r requirements.txt
mkdir -p data
echo "OPENAI_API_KEY=your_api_key_here" > .env

## Running the Agent

python -m app.agent

You will see a prompt:
tell me what to do:
Type a command, for example:
read file example.txt
The agent will respond using the available tools.

## Available Tools

get_file_content(file_path) - Read the content of a file (max characters: 10000)
get_files_info(directory) - List files and directories inside a given path
write_file(file_path, content) - Write content to a file (creates it if it doesn’t exist)
run_python_file(file_path, args) - Execute a Python file with optional arguments
delete_file(file_path) - Delete a single file
delete_folder(folder_path) - Delete a folder and all its contents

## Running Tests

pytest -q  # run all tests with minimal output
deepeval tst run evals/test_faithfulness.py
deepeval tst run evals/test_json_correctness.py
deepeval tst run evals/test_answer_relevancy.py

## Example Usage in Python

from app.agent import run_agent
response = run_agent("Read the file 'example.txt'")
print(response["summary"])

## Project Structure

openai-agent-playground/
├── app/
│   ├── agent.py          # Main agent code
│   ├── tools.py          # Custom agent tools
│   ├── config.py         # Configuration variables
├── data/                 # Working directory for agent operations
├── evals/                # DeepEval test cases
├── requirements.txt
├── README.md
├── .env                  # API key and other secrets

## Notes

- Only files inside `data/` can be accessed or modified.
- The agent can execute Python code and delete files, so use with care.
- DeepEval metrics allow you to measure correctness, faithfulness, and relevancy of outputs.

