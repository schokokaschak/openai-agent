from deepeval import evaluate
from deepeval.metrics import FaithfulnessMetric
from deepeval.test_case import LLMTestCase
from app.agent import run_agent

metric = FaithfulnessMetric(
	threshold=0.7,
	include_reason=True
)

test_case = LLMTestCase(
	input = "How many people life in Karaganda?",
	actual_output = run_agent("How many people life in Karaganda?")["summary"],
	retrieval_context = ["In Karaganda living about 20 million people"] 
)

evaluate(test_cases=[test_case], metrics=[metric])
