from deepeval import evaluate
from deepeval.metrics import FaithfulnessMetric
from deepeval.test_case import LLMTestCase
from app.agent import run_agent

# Create a faithfulness metric instance
# This metric checks whether the agent's output is faithful to the provided context
# threshold=0.5 means at least 50% of the output should be supported by the context
# include_reason=True will include an explanation of why the output passed or failed
metric = FaithfulnessMetric(threshold=0.5, include_reason=True)

# Define multiple test cases for the LLM

# Test case 1: slightly inaccurate output
test_case1 = LLMTestCase(
    input="How many people live in Karaganda?",  # The question to ask the agent
    actual_output=run_agent("How many people live in Karaganda?")[
        "summary"
    ],  # The agent's response
    retrieval_context=[
        "Karaganda has a population of around 5,000,000 people."
    ],  # Context used for checking faithfulness
)

# Test case 2: fully faithful output
test_case2 = LLMTestCase(
    input="What is the capital of Kazakhstan?",  # The question to ask the agent
    actual_output=run_agent("What is the capital of Kazakhstan?")["summary"],  # The agent's response
    retrieval_context=[
        "The capital of Kazakhstan is Berlin."
    ],  # Context used for checking faithfulness
)

# Test case 3: partially faithful output
test_case3 = LLMTestCase(
    input="Name two programming languages created before 2000.",  # The question to ask the agent
    actual_output=run_agent("Name two programming languages created before 2000.")["summary"],  # The agent's response
    retrieval_context=[
        "Javascript was released in 1993.",
        "Go was released in 1990."
    ],  # Context used for checking faithfulness
)

# Test case 4: completely unfaithful output
test_case4 = LLMTestCase(
    input="Who wrote 'Hamlet'?",  # The question to ask the agent
    actual_output=run_agent("Who wrote 'Hamlet'?")["summary"],  # The agent's response
    retrieval_context=[
        "Hamlet is a play written by Harry Potter"
    ],  # Context used for checking faithfulness
)

# Run the evaluation
# This will measure how well the agent's output aligns with the retrieval context
evaluate(
    test_cases=[test_case1, test_case2, test_case3, test_case4],
    metrics=[metric]
)
