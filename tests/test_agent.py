"""A test script to run a multi-agent workflow that processes meeting notes through three specialized agents.
This module orchestrates a three-stage AI agent pipeline:
1. Data Collector Agent: Reads and extracts meeting notes from a file
2. Insights Generator Agent: Analyzes the collected notes to generate insights
3. Standup Summarizer Agent: Creates a daily standup summary from the insights
The workflow uses Google ADK (Agent Development Kit) with an in-memory session service
and includes comprehensive logging to track execution flow and errors.

 """

import argparse
import asyncio
import logging
import os
from pathlib import Path
from typing import Optional

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from google.adk.plugins.logging_plugin import LoggingPlugin

from smart_work_agent.constants import APP_NAME, SESSION_ID, USER_ID
from smart_work_agent.agents.data_collector_agent import data_agent
from smart_work_agent.agents.insights_generator_agent import insight_agent
from smart_work_agent.agents.standup_summarizer_agent import standup_agent

try:
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise EnvironmentError("GOOGLE_API_KEY environment variable not set.")
    print("Gemini API key setup complete.")
except Exception as e:
    print(f"Authentication Error: Please make sure you have added 'GOOGLE_API_KEY'. Details: {e}")

# ---------------- Logging ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "logs", "loggers.log")
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.DEBUG,
    format="%(filename)s:%(lineno)s %(levelname)s:%(message)s",
)

logging.info("Logging configured")
print("Logging configured")


def resolve_meeting_notes_path(path_str: str) -> Optional[str]:
    """Resolve a meeting notes path robustly.

    Checks (in order): absolute path, relative-to-script, a few common repo
    locations, then CWD fallback. Returns absolute path string or `None`.
    """
    p = Path(path_str)
    if p.is_absolute() and p.exists():
        return str(p)

    paths = (Path(BASE_DIR) / p).resolve()
    if paths.exists():
        return str(paths)

    alt_path = [
        Path(BASE_DIR) / "data" / p.name,
        Path(BASE_DIR).parent / "data" / p.name,
        Path.cwd() / p,
    ]
    for alt in alt_path:
        try:
            if alt.exists():
                return str(alt.resolve())
        except Exception:
            continue

    return None


async def main(meeting_notes_path: str = "../data/meeting_notes.txt") -> None:
   
    resolved = resolve_meeting_notes_path(meeting_notes_path)
    if not resolved:
        logging.error("Meeting notes file not found. Checked provided path and common locations.")
        print("Error: Meeting notes file not found. Checked provided path and common locations.")
        return

    meeting_notes_path = resolved
    logging.info("Using meeting notes file: %s", meeting_notes_path)
    print(f"Using meeting notes file: {meeting_notes_path}")

    session_service = InMemorySessionService()
    await session_service.create_session(user_id=USER_ID, session_id=SESSION_ID, app_name=APP_NAME)

    runner = Runner(app_name=APP_NAME, agent=data_agent, plugins=[LoggingPlugin()], 
                    session_service=session_service)

    # Data agent: ask the tool to read the file
    data_message = Content(parts=[Part(text=f"Use the file_reader tool to read the file '{meeting_notes_path}'. Return only the content.")])

    collected_text = ""
    for event in runner.run(user_id=USER_ID, 
                            session_id=SESSION_ID,
                            new_message=data_message):
        if getattr(event, "is_final_response", False):
            collected_text = event.content.parts[0].text
            if collected_text is not None:
                print("\n DATA COLLECTED:\n", collected_text)

    # Insight agent
    runner.agent = insight_agent
    insight_text = ""
    for event in runner.run(user_id=USER_ID,
                            session_id=SESSION_ID, 
                            new_message=Content(parts=[Part(text=f"Analyze these updates:\n{collected_text}")] )):
        if getattr(event, "is_final_response", False):
            insight_text = event.content.parts[0].text
            print("\n INSIGHTS GENERATED:\n", insight_text)

    # Standup agent
    runner.agent = standup_agent
    summary_text = ""
    for event in runner.run(user_id=USER_ID, 
                            session_id=SESSION_ID,
                             new_message=Content(parts=[Part(text=f"Produce daily standup summary:\n{insight_text}")] )):
        if getattr(event, "is_final_response", False):
            summary_text = event.content.parts[0].text
            print("\n STANDUP SUMMARY:\n", summary_text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run multi-agent workflow for meeting notes.")
    parser.add_argument("--meeting_notes_path", type=str, 
                        default="../data/meeting_notes.txt", 
                        help="Path to the meeting notes file.")
    args = parser.parse_args()
    try:
        asyncio.run(main(args.meeting_notes_path))
    except Exception as e:
        logging.exception("Unhandled exception occurred during agent workflow execution.")
        print(f"Unhandled exception: {e}")
