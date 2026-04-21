def clean_diff(diff: str, max_chars: int = 3000) -> str:
    lines = diff.splitlines()

    filtered = [
        line for line in lines
        if line.startswith("+") or line.startswith("-")
    ]

    cleaned = "\n".join(filtered)

    return cleaned[:max_chars]