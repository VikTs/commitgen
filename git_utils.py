import subprocess

def get_git_diff():
    result = subprocess.run(
        ["git", "diff", "--staged"],
        capture_output=True,
        text=True
    )
    return result.stdout

def commit(message: str):
    subprocess.run(["git", "commit", "-m", message])