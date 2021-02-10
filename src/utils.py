import regex


def fastRegex(pattern: str, text: str) -> str:
    try:
        return regex.compile(pattern, regex.MULTILINE).search(text)[1]
    except TypeError:
        return ""

