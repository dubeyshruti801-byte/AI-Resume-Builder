def sanitize_text(text) -> str:
    """
    Clean a single value (string, int, float, etc.):
    - Convert to string if not None
    - Strip whitespace, remove newlines, normalize spaces
    """
    if text is None:
        return ""
    text = str(text)  # ✅ convert non-strings to string
    cleaned = text.strip()
    cleaned = cleaned.replace("\n", " ").replace("\r", " ")
    cleaned = " ".join(cleaned.split())  # collapse multiple spaces
    return cleaned


def sanitize_data(data):
    """
    Recursively sanitize input data (dict, list, str, int, float).
    - If str/int/float → clean it
    - If list → sanitize each item
    - If dict → sanitize each value
    - Otherwise → return as is
    """
    if isinstance(data, (str, int, float)):
        return sanitize_text(data)
    elif isinstance(data, list):
        return [sanitize_data(item) for item in data]
    elif isinstance(data, dict):
        return {key: sanitize_data(value) for key, value in data.items()}
    else:
        return data
