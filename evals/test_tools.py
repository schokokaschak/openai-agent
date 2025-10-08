'''from deepeval import evaluate
from deepeval.metrics import JsonCorrectnessMetric
from deepeval.test_case import LLMTestCase
from app.agent import ReturnSchema, run_agent

metric = JsonCorrectnessMetric(
    expected_schema=ReturnSchema,
    model="gpt-4.1",
    include_reason=True
)

test_case = LLMTestCase(
    input="Output me a random JSON with the 'name' key",
    actual_output=str(run_agent("Output me a random JSON with the 'name' key"))
)

evaluate(test_cases=[test_case], metrics=[metric])
'''