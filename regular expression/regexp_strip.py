def regex_strip(text: str, letters: str = None)-> str:
    import re
    if letters is None:
        left_strip_regex = re.compile(r"(^\s+)")
        right_strip_regex = re.compile(r"(\s+$)")
    else:
        left_strip_regex = re.compile(f"(^[{letters}]+)")
        right_strip_regex = re.compile(f"([{letters}]+$)")

    text = left_strip_regex.sub("", text)
    text = right_strip_regex.sub("", text)

    return text


print(regex_strip("  this is a test  -"))



