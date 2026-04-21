def build_prompt(diff: str) -> str:
    return f"""
Write a Conventional Commit message based ONLY on the git diff.

Rules:
- format: type(scope): short description
- max 70 characters
- no explanation
- no punctuation at the end
- be specific about code changes
- prefer verbs: add, fix, update, remove, refactor

Examples:
feat(profile): add user profile page
fix(api): handle empty API response
chore(deps): update dependencies

Git diff:
{diff}
"""