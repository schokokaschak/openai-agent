from agents import Agent, Runner
from dotenv import load_dotenv
load_dotenv()
from tools import get_file_content, get_files_info, write_file, run_python_file, delete_file, delete_folder

def run_agent(prompt: str) -> dict:
    try:
        agent = Agent(
        name="Assistant",
        instructions=(
            "You are a helpful assistant that can read, write, and execute files. "
            "You have access to tools like get_file_content, get_files_info, write_file, "
            "run_python_file, delete_folder, and delete_file."
        ),
        tools=[get_file_content, get_files_info, write_file, run_python_file, delete_folder, delete_file],
        )   

        result = Runner.run_sync(agent, prompt)
        if isinstance(result.final_output, dict):
            return result.final_output
        return {"summary": str(result.final_output)}

    except Exception as e:
        return {"error": str(e)}


def main():
    print("Hello from openai-agent!")
    prompt = input("tell me what to do: ")
    result = run_agent(prompt)
    print(result)

if __name__ == "__main__":
    main()
    