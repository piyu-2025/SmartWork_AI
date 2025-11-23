# Smart Work AI Tests

This directory contains integration tests for the `smart_work_agent`.

## How to Run

You can run the test from the root of the project using the following command:

```bash
python -m tests.test_agent
```

## Test Scenario

The `test_agent.py` script is an integration test that runs the `smart_work_agent` This project uses a file-reader tool that loads meeting notes from a local text file and feeds them into a multi-agent workflow:
### Data Collector Agent – 
reads file (meeting_notes.txt)
### Insight Generator Agent – 
generates risks, highlights, next steps
### Standup Composer Agent – 
produces polished daily standup
