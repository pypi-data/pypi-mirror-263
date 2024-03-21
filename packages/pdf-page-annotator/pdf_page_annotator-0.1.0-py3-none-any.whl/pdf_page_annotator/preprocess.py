import re


def remove_double_spaces(text: str) -> str:
    return re.sub(r'\s+', ' ', text)