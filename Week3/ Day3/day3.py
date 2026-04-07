def count_text_stats(text):
    lines = text.splitlines()
    words = text.split()
    chars = len(text)
    return len(lines), len(words), chars

def remove_empty_lines(text):
    lines = [line for line in text.splitlines() if line.strip()]
    return "\n".join(lines)

def parse_name_lines(text):
    result = {}
    for line in text.splitlines():
        if not line.strip():
            continue
        name, score = line.split(":", 1)
        result[name.strip()] = int(score.strip())
    return result

def append_log(path, message):
    with open(path, "a", encoding = "utf-8") as f:
        f.write(message + "\n")

def average_score(scores):
    if not scores:
        return 0
    return sum(scores)/len(scores)

def save_text(path, text):
    with open(path, "w", encoding = "utf-8") as f:
        f.write(text)
