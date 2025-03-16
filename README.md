# Practice GitHub Actions

## Requirements
- Python 3.x
- `git` installed

## Setup

1. Create a virtual environment:
   ```
   python -m venv .venv
   ```

2. Activate the virtual environment:
   - **macOS/Linux**:
     ```
     source .venv/bin/activate
     ```
   - **Windows**:
     ```
     .venv\Scripts\activate
     ```

3. Upgrade `pip`:
   ```
   pip install --upgrade pip
   ```

4. Install dependencies and run unit tests:
   ```
   python -m unittest discover -s . -p "test_*.py"
   ```

## Usage

### CLI Usage

To validate commit messages directly:

- **Valid message:**
  ```
  python linter.py "feat(auth): add login feature"
  ```
  
- **Invalid message (no colon):**
  ```
  python linter.py "invalid commit message"
  ```
  
- **Invalid message (too short):**
  ```
  python linter.py "fix:short"
  ```

### HTTP Server

To run the app as an HTTP server:

```
python src\main.py --server --port 8080
```

This will start a server on `http://127.0.0.1:8080`.

### Validate All Commits

To lint all commits in the repository:

```
python src\main.py --validate-log
```

This will evaluate all commit messages in your git history and print whether they are valid or invalid.

### Manually Test API

To manually test the API with `curl`:

- **Successful Call** (valid commit message):
  ```
  curl -X POST http://127.0.0.1:8080/validate -H "Content-Type: application/json" -d '{"message": "feat(auth): add login feature"}'
  ```

  **Response**:
  ```
  {"valid": true, "reason": ""}
  ```

- **Failed Call** (invalid commit message):
  ```
  curl -X POST http://127.0.0.1:8080/validate -H "Content-Type: application/json" -d '{"message": "feat(auth): add"}'
  ```

  **Response**:
  ```
  {"valid": false, "reason": "Too short message"}
  ```

## Testing

Run unit tests to ensure everything works:

```
python -m unittest src/test_linter.py -v
```
