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

# 🧠 LLM Evaluation Tests

This project contains several automated tests run with [DeepEval](https://github.com/confident-ai/deepeval).  
The goal is to evaluate the behavior of the agent (`run_agent`) and ensure that its responses are consistent, accurate, and contextually faithful.  
Each test assesses different quality aspects of the LLM outputs.

---

## 🔹 1. Faithfulness Tests (`test_faithfulness.py`)
**Goal:**  
Checks whether the agent's answers are **faithful to the provided retrieval context**.  
The test does **not** evaluate real-world truth, only whether the output **only uses information present in the context**. 
You can change the retrievel context in the app/config.py file.

**Expected Outcome:**  
- If the agent only reproduces information from the context → ✅ **Test passes**  
- If the agent adds new or conflicting information → ❌ **Test fails**

---

## 🔹 2. GEval Tests (`test_geval.py`)
**Goal:**  
Evaluates the **correctness of the agent’s answers** against expected “golden” outputs.  
The test compares the input question, expected output, and the agent’s actual output.

**Expected Outcome:**  
- Agent gives the correct or semantically correct answer → ✅  
- Answer is incorrect or irrelevant → ❌  


---

## 🔹 3. JSON Correctness Tests (`test_json_correctness.py`)
**Goal:**  
Checks whether the agent outputs **valid JSON** conforming to a defined **Pydantic schema**.  
Ensures that structured outputs are machine-readable and correctly formatted.

**Expected Outcome:**  
- Output contains valid JSON with all required schema fields → ✅  
- Formatting errors or structural mismatches → ❌  

These tests are especially useful for agents producing structured data (e.g., for APIs or pipelines).

---

## 🔹 4. Answer Relevancy Tests (`test_relevance.py`)
**Goal:**  
Measures how **relevant the agent's statements** are with respect to the input question.  
Irrelevant or off-topic information lowers the score.

**Expected Outcome:**  
- Answer stays on-topic and contains no unrelated information → ✅  
- Answer drifts off-topic or contains irrelevant details → ❌  

These tests are useful to detect “over-talking” or hallucinations.

---

## ⚙️ Running the Tests

All tests can be executed together via the CLI:

```bash
pytest -q -s
```
or with 

```bash
deepeval test run evals/test_faithfilness.py
deepeval test run evals/test_golden.py
deepeval test run evals/test_json.py
deepeval test run evals/test_relevance.py
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
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|── test_json.py  
├── requirements.txt  
├── README.md  
├── .env.example          # you can store your API key here  


## Notes 

- Only files inside `data/` can be accessed or modified.  
- The agent can execute Python code and delete files, so use with care.  
- DeepEval metrics allow you to measure correctness, faithfulness, and relevancy of outputs.  
