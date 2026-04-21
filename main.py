from git_utils import get_git_diff, commit
from diff_parser import clean_diff
from ai import generate_commit, ask_to_commit
from rich import print

def main():
    diff = get_git_diff()

    if not diff:
        print("[red]No staged changes[/red]")
        return

    cleaned = clean_diff(diff)

    commit_msg = generate_commit(cleaned)

    print("\n[bold green]Generated commit:[/bold green]")
    print(f"[cyan]{commit_msg}[/cyan]")

    if ask_to_commit():
        commit(commit_msg)
        print("[green]Committed![/green]")
    else:
        print("[yellow]Commit cancelled[/yellow]")


if __name__ == "__main__":
    main()