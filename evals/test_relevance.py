from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from app.agent import run_agent

# Create an AnswerRelevancyMetric instance
# This metric measures the proportion of relevant statements in the output
# - 'threshold' defines the minimum relevancy score for passing
# - 'include_reason=True' makes the metric return a reason explaining its score
metric = AnswerRelevancyMetric(threshold=0.7, include_reason=True)

# Define a single test case for the agent
# - 'input' is the question asked to the agent
# - 'actual_output' is the agent’s response retrieved via run_agent
test_case1 = LLMTestCase(
    input="What is the capital of Germany?",
    actual_output=run_agent("What is the capital of Germany?")["summary"],
)

# Run the evaluation on the test case using the relevancy metric
evaluate(test_cases=[test_case1], metrics=[metric])
