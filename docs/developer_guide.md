# Developer Guide for Python API Client

### 1. Clone repo

Clone git repo into your local machine.

```bash
$ git clone git@github.com:streambird/streambird-python.git
```

### 2. Install required packages

If you use a virtual environment (via venv or conda), please activate it before installing the following packages.

_Python SDK v2+ supports only Python 3.6+_

```bash
$ pip install -r docs/dev_requirements.txt
```
### 3. Setup pre-commit

Assure pre-commit<sup>[1]</sup> is installed:
```bash
$ pre-commit --version
# pre-commit 2.11.1
```

Configure pre-commit for the repo:
```bash
pre-commit install
```
Now `pre-commit` will run automatically on `git commit`!

### 4. (Optional) VS Code Settings

Press `Cmd+Shift+P` to open Command Palette on VSCode to find **Preferences: Open Settings (JSON)**.

If you want to make those settings only apply to current workspace (not VS Code general), choose **Preferences: Open Workspace Settings (JSON)**

- Enables `pylint`<sup>[2]</sup> and `flake8`<sup>[3]</sup> as linters together
- Auto-formats python files on save according to `black`

Append following lines to the json file:
```json
"python.linting.enabled": true,
"python.linting.pylintEnabled": true,
"python.linting.flake8Enabled": true,
"python.formatting.provider": "black",
"[python]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "ms-python.python"
    },
```

In Python SDK we follow [Google's Python Docstring Guide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) for comments and docstring of modules, functions and classes. [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) is a useful VS Code extension that helps to generate docstrings.

#### Install pip package locally

```bash
pip install -e .
```

### 5. Running pre-commit Tests Manually

You can run following command to run pre-commit linter for all files, without a commit. It provides a report for issues as well as fixes formatting.

```bash
$ pre-commit run --all-files

Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Passed
Check for added large files..............................................Passed
Check Yaml...............................................................Passed
Check for case conflicts.................................................Passed
isort....................................................................Passed
black....................................................................Passed
flake8...................................................................Passed
pylint...................................................................Passed
```

### 6. Running pytest Test Cases

Before pushing your code changes, you can run `pytest` to test existing cases. You can add new test cases if you're adding a new method or functionality to be tested.

In order to run `pytest` you need to set environment variable `STREAMBIRD_TEST_API_KEY` as your Streambird user's test key.

```bash
$ STREAMBIRD_TEST_API_KEY="{apikey}" python3 -m pytest -v
```

#### 7. Deployment and Publishing of a new version

Please refer to [Deployment and Publishing Guide](pypi_update_guide.md) for details.
_____
<sup>[1] pre-commit configuration is available in `.pre-commit-config.yaml`</sup>

<sup>[2] Pylint configuration is available in `.pylintrc`</sup>

<sup>[3] flake8 configuration is available in `setup.cfg`</sup>
