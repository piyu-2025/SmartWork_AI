"""File Reader Tool (file_reader_tool) — Module docstring
Reads the contents of a specified file.
Args:
    params (dict): A dictionary containing the filename under the key "filename".
        If not provided, defaults to "meeting_notes.txt".
Returns:
    str: The contents of the file if successfully read.
Exceptions:
    Prints an error message if the file is not found or if any other exception occurs during reading.
"""

# ---------------- File Reader Tool ----------------

def file_reader_tool(params: dict):
    try:
        filename = params.get("filename", "meeting_notes.txt")
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError as e:
        print("File 'meeting_notes.txt' not found {e}")
    
    except Exception as e:
        print("Error encountered while reading the file. Error details {e}")
    
