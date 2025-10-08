from deepeval import evaluate
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import GEval
from deepeval.dataset import EvaluationDataset, Golden
from app.agent import run_agent

metric = GEval(
    name="Correctness",
    criteria="Determine of the 'actual output' is correct based on the 'expected output'. It has to be correct on it's essence."
    "Ignore format issues.",
    evaluation_params=[
        LLMTestCaseParams.ACTUAL_OUTPUT,
        LLMTestCaseParams.EXPECTED_OUTPUT,
    ],
    threshold=0.5,
)

goldens = [
    Golden(input="What is the capital of France?", expected_output="Paris"),
    Golden(input="What is 14 * 1?", expected_output="14"),
]

dataset = EvaluationDataset(goldens=goldens)

for golden in dataset.goldens:
    dataset.add_test_case(
        LLMTestCase(
            input=golden.input,
            expected_output=golden.expected_output,
            actual_output=run_agent(golden.input)["summary"],
        )
    )
evaluate(test_cases=dataset.test_cases, metrics=[metric])
