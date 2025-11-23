"""
Standup Agent (standup_agent) — Module docstring
This module defines the standup_agent, an instance of LlmAgent configured to generate daily standup summaries in agile and Jira style.
The agent acts as a technical lead and scrum master, producing polished summaries from provided insights and highlighting whether tasks should be handled by the whole team or specific members (senior or junior).
"""

from google.adk.agents import LlmAgent
from smart_work_agent.constants import MODEL
from smart_work_agent.tools.date_time_tool import date_time_tool

# ---------------- Standup Agent ----------------
standup_agent = LlmAgent(
    model=MODEL,
    name="standup_summary_generator",
    description="""You are technical lead and scrum master.
    Add dates of the summary taking from tool get_current_date
    Generate a polished daily standup summary from insights in agile and Jira style.
    Also highlight if it has to be handled by the whole team or a single team member(senior or junior).
    """,
    tools=[date_time_tool]
)