## Setup python-semantic-release for Your Python Project

### 1. Setup python-semantic-release for Your Python Project
```shell
pip install python-semantic-release
```

### 2. Add __version__ to your code
```python
__version__ = "1.0.0"
```

### 3. Create Configuration file pyproject.toml (recommended if using modern tools)
```toml
[tool.semantic_release]
version_variable = "main.py:__version__"
branch = "main"
upload_to_pypi = false
changelog_file = "CHANGELOG.md"
build_command = ""
```


### 4. GitHub Action Workflow:
Create .github/workflows/release.yml:
```yaml
name: Python Semantic Release

on:
  push:
    branches:
      - main

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install python-semantic-release

      - name: Run semantic-release
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: semantic-release publish
```


### 5. Use Conventional Commits
Ensure all your commit messages follow this format:
```
feat: add something
fix: correct a bug
chore: minor cleanup
docs: update README
```


### 6. Other Pre-reqs
1: Set GH_TOKEN or GITHUB_TOKEN environment variable

in bash terminal
```bash
export GH_TOKEN=ghp_YourGitHubTokenHere
```

or in Windows CMD
```cmd
set GH_TOKEN=ghp_YourGitHubTokenHere
```


### 7. First Manual Version Bump (optional)
Run this once to verify version bump locally:

```bash
semantic-release version
```
This will:
Updates __version__
Creates CHANGELOG.md



### 8. Common Release Workflow
```
# Step 1: Analyze commits and update CHANGELOG.md
semantic-release changelog

# Step 2: Bump version and create a tag
semantic-release version

# Push your commits and tags to GitHub
git push && git push --tags

# Step 3: Create GitHub release (and publish if configured)
semantic-release publish
```

### 9. Issues

```shell
$ semantic-release version
::ERROR:: 'charmap' codec can't decode byte 0x90 in position 138: character maps to <undefined>
Run semantic-release in very verbose mode (-vv) to see the full traceback.
```

Set environment variable PYTHONUTF8=1
Force Python to use UTF-8 encoding regardless of system locale:

In PowerShell:
```powershell
$env:PYTHONUTF8=1
semantic-release version
```

In Windows CMD:
```cmd
set PYTHONUTF8=1
semantic-release version
```

In BASH
```bash
export PYTHONUTF8=1
semantic-release version
```