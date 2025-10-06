from agents import Agent, Runner
from dotenv import load_dotenv
load_dotenv()


def main():
    print("Hello from openai-agent!")
    agent = Agent(name="Assistant", instructions="You are a helpful assistant")
    
    result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
    print(result.final_output)
    print(result)

if __name__ == "__main__":
    main()