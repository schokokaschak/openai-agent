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

# Load environment variables from the .env file
load_dotenv()


def run_agent(prompt: str) -> dict:
    """
    Run the OpenAI agent synchronously and return the result as a dictionary.

    Args:
        prompt (str): The user input or task description

    Returns:
        dict: Contains the agent's final output under 'summary'
              or an 'error' key if something goes wrong.
    """
    try:
        # Initialize the agent with a name, instructions, and the tools it can use
        agent = Agent(
            name="Assistant",
            instructions=system_prompt,
            tools=[
                get_file_content,
                get_files_info,
                write_file,
                run_python_file,
                delete_folder,
                delete_file,
            ],
        )

        # Run the agent synchronously and get the result
        result = Runner.run_sync(agent, prompt)

        # Prepare the result for returning
        finish = dict()
        finish["summary"] = str(result.final_output)  # Convert the agent's output to a string
        return finish

    except Exception as e:
        # Return error text if something goes wrong
        return {"error": str(e)}


def main():
    """
    Main function for the command line interface.
    Prompts the user for input, runs the agent, and prints the result.
    """
    print("Hello from openai-agent!")
    prompt = input("tell me what to do: ")  # Ask the user for a prompt
    result = run_agent(prompt)  # Execute the agent
    print(result)  # Print the agent's output to the console


# Only run this if the script is executed directly
if __name__ == "__main__":
    main()
