from deepeval import evaluate
from deepeval.test_case import LLMTestCase, ToolCall
from deepeval.metrics import ToolCorrectnessMetric
from app.agent import run_agent


test_case = LLMTestCase(
    input="which files are inside my dir?",
    actual_output="We offer a 30-day full refund at no extra cost.",
    # Replace this with the tools that was actually used by your LLM agent
    tools_called=[ToolCall(name="WebSearch"), ToolCall(name="ToolQuery")],
    expected_tools=[extract_tool_calls("which files are inside my dir?")],
)
metric = ToolCorrectnessMetric()

evaluate(test_cases=[test_case], metrics=[metric])