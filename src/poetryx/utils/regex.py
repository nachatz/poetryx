import re

def regex_search(regex: str, input: str) -> str:
    match = re.search(rf'{regex}', input)
    if match:
        return match.group(1)
    else:
        raise ValueError(f"Unable to match {regex} in {input}")