from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from app.agent import run_agent

# Create an AnswerRelevancyMetric instance
# This metric measures the proportion of relevant statements in the output
# - 'threshold' defines the minimum relevancy score for passing
# - 'include_reason=True' makes the metric return a reason explaining its score
metric = AnswerRelevancyMetric(threshold=0.7, include_reason=True)

# Define multiple test cases for the agent
# - 'input' is the question asked to the agent
# - 'actual_output' is the agent’s response retrieved via run_agent

# Test case 1: straightforward factual question (expected high relevancy)
test_case1 = LLMTestCase(
    input="What is the capital of Germany?",
    actual_output=run_agent("What is the capital of Germany?")["summary"],
)

# Test case 2: question with potential for irrelevant extra info (expected partial relevancy)
test_case2 = LLMTestCase(
    input="Who discovered penicillin?",
    actual_output=run_agent("Who discovered penicillin?")["summary"],
)

# Test case 3: agent may include unrelated commentary (expected low relevancy)
test_case3 = LLMTestCase(
    input="What is the square root of 64?",
    actual_output=run_agent(
        "What is the square root of 64? Please dont explain too much."
    )["summary"],
)

# Test case 4: longer, multi-part question where some parts may be missed
test_case4 = LLMTestCase(
    input="Name two planets in our solar system and briefly describe one of them.",
    actual_output=run_agent(
        "Name two planets in our solar system and briefly describe one of them."
    )["summary"],
)

# Test case 5: off-topic generation (expected fail)
test_case5 = LLMTestCase(
    input="What is Python used for?",
    actual_output=run_agent(
        "What is Python used for? Tell me also a funny joke about cats."
    )["summary"],
)

# Test case 6: abstract or open-ended question (tests semantic relevance)
test_case6 = LLMTestCase(
    input="Why is time management important?",
    actual_output=run_agent("Why is time management important?")["summary"],
)

# Run the evaluation on all test cases using the relevancy metric
evaluate(
    test_cases=[test_case1, test_case2, test_case3, test_case4, test_case5, test_case6],
    metrics=[metric],
)
