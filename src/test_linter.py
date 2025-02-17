import unittest
from linter import validate_commit_message

class TestCommitMessageLinter(unittest.TestCase):

    def test_valid_commit_messages(self):
        # List of valid commit messages to test
        test_cases = [
            ("feat(auth): add login feature", ""),
            ("fix(ui): fix bug in UI", ""),
            ("chore(tests): refactor test cases", ""),
            ("docs(readme): update README file", ""),
            ("style(css): update button color", ""),
            ("perf(logging): improve performance of logging", ""),
            ("ci(github-actions): update workflows", ""),
            ("test(unit): add unit tests for login feature", ""),
        ]
        
        for msg, expected_reason in test_cases:
            result, reason = validate_commit_message(msg)
            self.assertTrue(result, 
                f"Test Failed \nCommit: '{msg}'\nExpected Valid\nActual Reason: '{reason}'")

    def test_valid_commit_message_with_extra_spaces(self):
        # List of valid commit messages with extra spaces
        test_cases = [
            ("feat(auth):    add login feature   ", ""),
            ("docs(readme):           update README file", ""),
            ("fix(ui): fix bug in UI              ", ""),
        ]
        
        for msg, expected_reason in test_cases:
            result, reason = validate_commit_message(msg)
            self.assertTrue(result, 
                f"Test Failed \nCommit: '{msg}'\nExpected Valid\nActual Reason: '{reason}'")

    def test_valid_commit_message_with_extra_colons(self):
        # List of valid commit messages with extra colons
        test_cases = [
            ("feat(auth): add: login feature", ""),
            ("docs(readme): update README file : update Dev Notes", ""),
            ("fix(ui): fix bug in UI : completed task 1234", ""),
        ]
        
        for msg, expected_reason in test_cases:
            result, reason = validate_commit_message(msg)
            self.assertTrue(result, 
                f"Test Failed \nCommit: '{msg}'\nExpected Valid\nActual Reason: '{reason}'")


    def test_missing_colon(self):
        # Commit message without colon should fail with "Missing colon"
        msg = "feat(auth) add login feature"
        expected_reason = "Missing colon"
        result, reason = validate_commit_message(msg)
        self.assertFalse(result, 
            f"\nTest Failed - \nCommit: '{msg}'\nExpected Reason: '{expected_reason}'\nActual Reason: '{reason}'")
    
    def test_unclosed_parentheses(self):
        # Commit message with an open parenthesis but no closing one
        msg = "feat(auth: add login feature"
        expected_reason = "Invalid format (unclosed parentheses)"
        result, reason = validate_commit_message(msg)
        self.assertFalse(result, 
            f"\nTest Failed - \nCommit: '{msg}'\nExpected Reason: '{expected_reason}'\nActual Reason: '{reason}'")
    
    def test_empty_scope(self):
        # Commit message with empty parentheses should fail as missing scope
        msg = "feat(): add login feature"
        expected_reason = "Missing scope"
        result, reason = validate_commit_message(msg)
        self.assertFalse(result, 
            f"\nTest Failed - \nCommit: '{msg}'\nExpected Reason: '{expected_reason}'\nActual Reason: '{reason}'")
    
    def test_invalid_type(self):
        # Commit message with a type not in the allowed list
        msg = "update(auth): add login feature"
        expected_reason = "Missing type"
        result, reason = validate_commit_message(msg)
        self.assertFalse(result, 
            f"\nTest Failed - \nCommit: '{msg}'\nExpected Reason: '{expected_reason}'\nActual Reason: '{reason}'")

    def test_boundary_message_length(self):
        # Test commit with exactly 10 characters in the message body should pass
        msg = "feat(auth): 1234567890"  # 10 characters after colon
        result, reason = validate_commit_message(msg)
        self.assertTrue(result, 
            f"Test Failed \nCommit: '{msg}'\nExpected Valid\nActual Reason: '{reason}'")
        # Test commit with 9 characters should fail
        msg_fail = "feat(auth): 123456789"  # 9 characters only
        expected_reason = "Too short message"
        result, reason = validate_commit_message(msg_fail)
        self.assertFalse(result, 
            f"\nTest Failed - \nCommit: '{msg_fail}'\nExpected Reason: '{expected_reason}'\nActual Reason: '{reason}'")

if __name__ == "__main__":
    unittest.main(verbosity=2)
