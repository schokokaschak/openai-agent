from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from app.agent import run_agent

metric = AnswerRelevancyMetric(
	threshold=0.7,
	include_reason=True
	)

test_case1 = LLMTestCase(
	input = "What is the capital of Germany?",
	actual_output = run_agent("What is the capital of Germany?")["summary"]
		
)

evaluate(test_cases=[test_case1], metrics=[metric])





