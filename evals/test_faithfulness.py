from deepeval import evaluate
from deepeval.metrics import FaithfulnessMetric
from deepeval.test_case import LLMTestCase
from app.agent import run_agent

# Create a faithfulness metric instance
# This metric checks whether the agent's output is faithful to the provided context
# threshold=0.5 means at least 50% of the output should be supported by the context
# include_reason=True will include an explanation of why the output passed or failed
metric = FaithfulnessMetric(threshold=0.5, include_reason=True)

# Define a single test case for the LLM
test_case = LLMTestCase(
    input="How many people life in Karaganda?",  # The question to ask the agent
    actual_output=run_agent("How many people life in Karaganda?")["summary"],  # The agent's response
    retrieval_context=["In Karaganda living about 20 million people"],  # Context used for checking faithfulness
)

# Run the evaluation
# This will measure how well the agent's output aligns with the retrieval context
evaluate(test_cases=[test_case], metrics=[metric])
