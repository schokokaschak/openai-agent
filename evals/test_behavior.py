from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import FaithfulnessMetric
from app.agent import run_agent

def test_faith():
	# Replace this with the actual output from your LLM application
	actual_output = run_agent("Is there a file named example in my working dir. If yes whats the content of the file?")

	# Replace this with the actual retrieved context from your RAG pipeline
	retrieval_context = ["There is a file and the content is 123456789"]

	metric = FaithfulnessMetric(
		threshold=0.5,
		model="gpt-4o",
		include_reason=True
	)
	test_case = LLMTestCase(
		input="Is there a file named example in my working dir. If yes whats the content of the file?",
		actual_output=actual_output["summary"],
		retrieval_context=retrieval_context
)

	assert_test(test_case, [metric])



