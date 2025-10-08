from deepeval import evaluate
from deepeval.metrics import JsonCorrectnessMetric
from deepeval.test_case import LLMTestCase
from pydantic import BaseModel
from app.agent import run_agent

# Define the expected JSON schema for evaluation
class ExampleSchema(BaseModel):
    name: str

# Initialize the JsonCorrectness metric
metric = JsonCorrectnessMetric(
    expected_schema=ExampleSchema,
    model="gpt-4.1",
    include_reason=True
)

# First test case: LLM output without strict instructions
test_case = LLMTestCase(
    input="Output me a random Json with the 'name' key",
    # Replace this with the actual output from your LLM application
    actual_output=run_agent("Output me a random Json with the 'name' key")["summary"]
)

# Second test case: LLM output with strict instructions to produce JSON only
test_case2 = LLMTestCase(
    input="Output me a random Json with the 'name' key. don't write anything else. only the JSON without comments",
    # Replace this with the actual output from your LLM application
    actual_output=run_agent(
        "Output me a random Json with the 'name' key. don't write anything else. do not use ```json or other markdowns"
    )["summary"]
)

# To run the metric standalone:
# metric.measure(test_case)
# print(metric.score, metric.reason)

# Evaluate both test cases with the JsonCorrectness metric
evaluate(test_cases=[test_case, test_case2], metrics=[metric])
