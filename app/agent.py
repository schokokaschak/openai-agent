from agents import Agent, Runner
from dotenv import load_dotenv
load_dotenv()
from tools import get_file_content, get_files_info, write_file, run_python_file, delete_file, delete_folder

def main():
    print("Hello from openai-agent!")
    agent = Agent(name="Assistant", 
                  instructions="""You are a helpful assistant that can read files from disk "
								"when the user asks to open or summarize a file. "
								"You have access to some tools called like 'get_file_content' that takes one argument: "
								"'file_path'. then the tool get_files_info: Lists files in the specified directory along with their sizes, constrained to the working directory.
                                and write_file: Writes content to a file within the working directory. Creates the file if it doesn't exist.
                                next tool is run_python_file: Executes a Python file within the working directory and returns the output from the interpreter.
                                it takes Path to the Python file to execute, relative to the working directory. and Optional arguments to pass to the Python file.
								with delete_folder and delete_file you can delete files and folders.
                                """,
                  tools=[get_file_content, get_files_info, write_file, run_python_file, delete_folder, delete_file])
    prompt = input("tell me what to do:")
    result = Runner.run_sync(agent, prompt)
    print(result.final_output)
    print(result)

if __name__ == "__main__":
    main()
    