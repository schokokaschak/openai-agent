from agents import Agent, Runner
from dotenv import load_dotenv
from app.config import system_prompt
from app.tools import (
    get_file_content,
    get_files_info,
    write_file,
    run_python_file,
    delete_file,
    delete_folder,
)

load_dotenv()


def run_agent(prompt: str) -> dict:
    try:
        agent = Agent(
            name="Assistant",
            instructions=(system_prompt),
            tools=[
                get_file_content,
                get_files_info,
                write_file,
                run_python_file,
                delete_folder,
                delete_file,
            ],
        )
        result = Runner.run_sync(agent, prompt)

        finish = dict()
        finish["summary"] = str(result.final_output)
        return finish

    except Exception as e:
        return {"error": str(e)}


def main():
    print("Hello from openai-agent!")
    prompt = input("tell me what to do: ")
    result = run_agent(prompt)
    print(result)


if __name__ == "__main__":
    main()
