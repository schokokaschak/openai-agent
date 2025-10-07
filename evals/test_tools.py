
from deepeval import evaluate
from deepeval.test_case import LLMTestCase, ToolCall
from deepeval.metrics import ToolCorrectnessMetric
from app.agent import run_agent
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

test_case = LLMTestCase(
    input="Is there a file name example in my working folder. If yes what does it contain?",

    actual_output = run_agent("Is there a file name example in my working folder. If yes what does it contain?")["summary"],
    tools_called=[],
    expected_tools=[ToolCall(name="WebSearch")],
)
metric = ToolCorrectnessMetric()

evaluate(test_cases=[test_case], metrics=[metric])
