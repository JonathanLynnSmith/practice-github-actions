import re
import subprocess
import sys

def validate_commit_message(msg):
    # Ensure there is a colon in the message
    if ':' not in msg:
        return False, "Missing colon"
    
    # Extract the part before the colon
    type_scope = msg.split(":", 1)[0].strip()
    
    # Use regex to check for a valid type at the start
    valid_types = ["feat", "fix", "chore", "docs", "style", "refactor", "test", "ci", "perf"]
    m = re.match(r"^(feat|fix|chore|docs|style|refactor|test|ci|perf)", type_scope)
    if not m:
        return False, "Missing type"
    
    # Check for the presence of a scope in parentheses
    if '(' in type_scope:
        if ')' not in type_scope:
            return False, "Invalid format (unclosed parentheses)"
        scope_content = type_scope[type_scope.find("(")+1:type_scope.find(")")]
        if not scope_content:
            return False, "Missing scope"
    else:
        return False, "Missing scope"
    
    # Check if the message after the colon is long enough
    msg_body = msg.split(":", 1)[1].strip()
    if len(msg_body) < 10:
        return False, "Too short message"
    
    return True, ""

def get_commit_messages():
    try:
        # Run git log to get all commit messages
        result = subprocess.run(
            ["git", "log", "--pretty=format:%s"],  # Get the commit messages
            capture_output=True,
            text=True,
            check=True
        )
        # Split the output into a list of commit messages
        commit_messages = result.stdout.splitlines()
        return commit_messages
    except subprocess.CalledProcessError as e:
        print(f"Error getting commit messages: {e}")
        sys.exit(1)