""" Data Agent (data_agent) — Module docstring
Module that defines a preconfigured LLM-based data collection agent.
This module constructs and exposes a single LlmAgent instance intended to read
and ingest file contents via the provided file_reader_tool.

Usage:
    Import `data_agent` and invoke it through the LlmAgent's execution interface
    to perform file-reading tasks. The agent delegates file operations to
    file_reader_tool, so ensure that tool is available and appropriately
    configured in the runtime environment.
"""

from smart_work_agent.tools.file_reader_tool import file_reader_tool
from google.adk.agents import LlmAgent
from smart_work_agent.constants import MODEL

# ---------------- Data Agent ----------------
data_agent = LlmAgent(
    model=MODEL,
    name="data_collector",
    description="Read files using the file_reader tool. If the file has incorrect syntax, specify the correct syntax.",
    tools=[file_reader_tool]
)