from deepeval import evaluate
from deepeval.metrics import JsonCorrectnessMetric
from deepeval.test_case import LLMTestCase
from pydantic import BaseModel
from app.agent import run_agent


# Define the expected JSON schema for evaluation
# This model defines the expected structure of the output JSON
class ExampleSchema(BaseModel):
    name: str


# Example of a slightly more complex JSON schema
class UserSchema(BaseModel):
    name: str
    age: int
    email: str


# Example of a nested JSON schema
class NestedSchema(BaseModel):
    user: UserSchema
    active: bool


# Initialize the JsonCorrectness metric
metric = JsonCorrectnessMetric(
    expected_schema=ExampleSchema,  # Default schema used for simpler test cases
    model="gpt-4.1",
    include_reason=True,
)

# First test case: LLM output without strict instructions
test_case = LLMTestCase(
    input="Output me a random Json with the 'name' key",
    # Replace this with the actual output from your LLM application
    actual_output=run_agent("Output me a random Json with the 'name' key")["summary"],
)

# Second test case: LLM output with strict instructions to produce JSON only
test_case2 = LLMTestCase(
    input="Output me a random Json with the 'name' key. don't write anything else. only the JSON without comments",
    # Replace this with the actual output from your LLM application
    actual_output=run_agent(
        "Output me a random Json with the 'name' key. don't write anything else. do not use ```json or other markdowns"
    )["summary"],
)

# Third test case: JSON with multiple keys, using a stricter schema
metric_user = JsonCorrectnessMetric(
    expected_schema=UserSchema, model="gpt-4.1", include_reason=True
)
test_case3 = LLMTestCase(
    input="Generate a JSON with the keys 'name', 'age', and 'email'.",
    actual_output=run_agent(
        "Generate a JSON with the keys 'name', 'age', and 'email'."
    )["summary"],
)

# Fourth test case: Nested JSON structure
metric_nested = JsonCorrectnessMetric(
    expected_schema=NestedSchema, model="gpt-4.1", include_reason=True
)
test_case4 = LLMTestCase(
    input="Output a JSON with a 'user' object containing 'name', 'age', and 'email', and a boolean field 'active'.",
    actual_output=run_agent(
        "Output a JSON with a 'user' object containing 'name', 'age', and 'email', and a boolean field 'active'."
    )["summary"],
)

# Fifth test case: agent adds explanation text, should fail strict validation
test_case5 = LLMTestCase(
    input="Output a JSON with a single 'name' key.",
    actual_output=run_agent(
        "Output a JSON with a single 'name' key, but include a short explanation before it."
    )["summary"],
)

# To run the metric standalone:
# metric.measure(test_case)
# print(metric.score, metric.reason)

# Evaluate all test cases using their respective metrics
evaluate(
    test_cases=[test_case, test_case2],
    metrics=[metric],
)

evaluate(
    test_cases=[test_case3],
    metrics=[metric_user],
)

evaluate(
    test_cases=[test_case4],
    metrics=[metric_nested],
)

evaluate(
    test_cases=[test_case5],
    metrics=[metric],
)
