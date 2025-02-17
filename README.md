# practice-github-actions

## Setup
```shell
python -m venv .venv
```

```shell
source .venv/bin/activate  # On macOS/Linux
```

```shell
.venv\Scripts\activate  # On Windows
```

```shell
pip install --upgrade pip
```

```shell
python -m unittest discover -s . -p "test_*.py"
```

## Usage

```shell
python linter.py "feat(auth): add login feature"  # Should be valid
python linter.py "invalid commit message"         # Should be invalid
python linter.py "fix:short"                      # Should be invalid
```

# Manually Test API

Succesful Call
```shell
curl -X POST http://127.0.0.1:8000/validate -H "Content-Type: application/json" -d '{"message": "feat(auth): add login feature"}'

# Returns --> {"valid":true,"reason":""}
```

Failed Call
```shell
curl -X POST http://127.0.0.1:8000/validate -H "Content-Type: application/json" -d '{"message": "feat(auth): add"}'

# Returns --> {"valid":false,"reason":"Too short message"}
```