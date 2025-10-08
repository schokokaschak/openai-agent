from deepeval import evaluate
from deepeval.metrics import JsonCorrectnessMetric
from deepeval.test_case import LLMTestCase
from pydantic import BaseModel
from app.agent import run_agent

class ExampleSchema(BaseModel):
    name: str

metric = JsonCorrectnessMetric(
    expected_schema=ExampleSchema,
    model="gpt-4.1",
    include_reason=True
)
test_case = LLMTestCase(
    input="Output me a random Json with the 'name' key",
    # Replace this with the actual output from your LLM application
    actual_output=run_agent("Output me a random Json with the 'name' key")["summary"]
)

test_case2 = LLMTestCase(
    input="Output me a random Json with the 'name' key. dont write anything else. only the json without your comments",
    # Replace this with the actual output from your LLM application
    actual_output=run_agent("Output me a random Json with the 'name' key. dont write anything else. do not use ``` json or other markdowns")["summary"]
)

# To run metric as a standalone
# metric.measure(test_case)
# print(metric.score, metric.reason)

evaluate(test_cases=[test_case, test_case2], metrics=[metric])