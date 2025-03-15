import argparse
import sys
from api import app  # Import the Flask app from api.py
from linter import validate_commit_message, get_commit_messages  # Import linting functions
from colorama import init, Fore  # Import colorama for coloring output

# Initialize colorama
init(autoreset=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate commit messages via CLI or HTTP server.")
    parser.add_argument("message", nargs="?", help="Commit message to validate")
    parser.add_argument("--server", action="store_true", help="Run as an HTTP server")
    parser.add_argument("--port", type=int, default=8080, help="Port for HTTP server (default: 8080)")
    parser.add_argument("--validate-log", action="store_true", help="Lint all previous commits in the repo")

    args = parser.parse_args()

    if args.server:
        # Run Flask app from api.py
        app.run(host="0.0.0.0", port=args.port)
    elif args.validate_log:
        # Run linter on all commit messages in the repo
        commit_messages = get_commit_messages()  # Fetch all commit messages
        for commit in commit_messages:
            is_valid, error_message = validate_commit_message(commit)
            if is_valid:
                print(f"{Fore.GREEN}VALID -> {commit}")
            else:
                print(f"{Fore.RED}INVALID -> {commit} -> {error_message}")
    elif args.message:
        # Run linter in CLI mode
        is_valid, error_message = validate_commit_message(args.message)
        if is_valid:
            print(f"{Fore.GREEN}Commit message is valid.")
            sys.exit(0)
        else:
            print(f"{Fore.RED}Invalid commit message: {error_message}")
            sys.exit(1)
    else:
        print("Usage: validate_commit <commit_message> OR validate_commit --server OR validate_commit --lint-all")
        sys.exit(1)
