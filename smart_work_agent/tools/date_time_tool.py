
from datetime import datetime
""" Date Time Tool (date_time_tool) — Module docstring
Return the current local date and time as an ISO 8601 formatted string.

This function uses datetime.now() to obtain the current local date and time
and returns it as an ISO 8601 compliant string produced by datetime.isoformat().
"""
def date_time_tool():
    return datetime.now().isoformat()