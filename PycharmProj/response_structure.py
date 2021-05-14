
def get_boolean(query: str) -> str:
    if "on" in query or "activate" in query:
        return "on"
    if "off" in query or "deactivate" in query:
        return "off"
    return "null"
