# OpenAI Agent

An interactive AI assistant that can read, write, execute, and delete files within a controlled working directory. Includes custom tools and supports automated evaluation using DeepEval.

## Features

- Read file contents
- List files and directories
- Write to files
- Execute Python scripts
- Delete files or directories
- Testable with DeepEval metrics: Faithfulness, JSON correctness, Answer relevancy, GEval

## Installation & Setup
```bash

git clone https://github.com/schokokaschak/openai-agent.git
cd openai-agent
```

# Create and activate a virtual environment using uv
```bash
uv venv .venv
source .venv/bin/activate  # macOS/Linux
```
# Install dependencies from requirements.txt
```bash
uv pip install -r requirements.txt
```

# Add your OpenAI API key
You need a API key run the agent. 
```bash
echo "OPENAI_API_KEY=your_api_key_here" > .env
```
# app/config.py

Here you can change three variables that are used by the agent. 

-> MAX_CHARS: its the maximum on characters we can read with our get_file_content function  
-> WORK_DIR: here we tell the agent in which folder he can work (read, write, delete, execute .py files)  
-> system_prompt: Instructions for the agent — this tells it what it is allowed to do and what tools it can use.  

## Running the Agent
```bash
python -m app.agent
```
You will see a prompt:
tell me what to do:

Type a command, for example:
read file example.txt

The agent will respond using the available tools.

## Available Tools

get_file_content(file_path) - Read the content of a file  
get_files_info(directory) - List files and directories inside a given path  
write_file(file_path, content) - Write content to a file (creates it if it doesn’t exist)  
run_python_file(file_path, args) - Execute a Python file with optional arguments  
delete_file(file_path) - Delete a single file  
delete_folder(folder_path) - Delete a folder and all its contents  

## Running Tests
```bash
pytest -q -s # run all tests with output
```

or run deepeval tests 
```bash
deepeval test run evals/test_faithfulness.py
deepeval test run evals/test_tools.py
deepeval test run evals/test_relevance.py
deepeval test run evals/golden.py
```

## Project Structure

openai-agent/  
├── app/  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── agent.py          # Main agent code  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── tools.py          # Custom agent tools  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── config.py         # Configuration variables  
├── data/                 # Working directory for agent operations  
├── evals/                # DeepEval test cases  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|── test_faithfulness.py  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|── test_golden.py  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|── test_relevance.py  
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|── test_tools.py  
├── requirements.txt  
├── README.md  
├── .env.example          # you can store your API key here  


## Notes 

- Only files inside `data/` can be accessed or modified.  
- The agent can execute Python code and delete files, so use with care.  
- DeepEval metrics allow you to measure correctness, faithfulness, and relevancy of outputs.  
