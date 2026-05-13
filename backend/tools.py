from langchain.tools import tool
from drive_service import search_drive_files


@tool

def drive_search_tool(query: str):
    """
    Search Google Drive files using Google Drive q parameter.
    """

    files = search_drive_files(query)

    if not files:
        return "No matching files found."

    result = []

    for file in files:
        result.append(
            f"""
Name: {file['name']}
Type: {file['mimeType']}
Modified: {file['modifiedTime']}
Link: {file['webViewLink']}
"""
        )

    return "\n".join(result)