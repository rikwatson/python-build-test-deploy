# Example Python Test CI/CD Project

## Tools

* [pyenv](www.example.com) for Python Environment management
* Editor / lightweight IDE [PyCharm](https://www.jetbrains.com/pycharm/) or [VSCode](https://code.visualstudio.com/)


## Supported Dev Platforms

* macOS
* Linux (Ubuntu)
* Windows via Linux (follow Linux instructions): [WSL (Ubuntu)](https://docs.microsoft.com/en-us/windows/wsl/install-win10) | [VS Code Remote Containers](https://code.visualstudio.com/docs/remote/containers)

## Getting started

### Prerequisites

#### Python Environment Management

* [pyenv](https://github.com/pyenv/pyenv) with:
  * [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) and
  * [pyenv-which-ext](https://github.com/pyenv/pyenv-which-ext)

##### macOS

```bash
brew install pyenv
brew install pyenv-virtualenv
brew install pyenv-which-ext
```

Add this to the _end_ of your `.bash_profile` / `.bashrc` / `.zshrc` / etc and `source` it:

```bash
export PYENV_VIRTUALENV_DISABLE_PROMPT=0
export PATH="$HOME/.poetry/bin:$PATH"
if [[ -z "$VIRTUAL_ENV" ]]; then
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
fi
```

#### [Python](https://www.python.org/) 3.8.x or 3.9.x

##### macOS & Ubuntu
  
```bash
pyenv install 3.9.5
```

Verify that it installed and is available to pyenv:

```bash
pyenv versions
```

You should see something like this:

```bash
* system
  3.9.5
```

### Python Packaging & Dependency Management

* Python [Poetry](https://rikwatson.github.io/python_poetry/)

#### On macOS & Ubuntu

```bash
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# This is the recommended way to install Poetry to ensure it is isolated from the rest of your system by vendorizing its dependencies.
```

Add this to your `.bash_profile` / `.bashrc` / `.zshrc` / etc _after_ the `pyenv` config you added above:

```bash
export PATH="$HOME/.poetry/bin:$PATH”
```

The _bottom_ of your *rc file should now look like this (including pyenv config steps from above)

```bash
export PYENV_VIRTUALENV_DISABLE_PROMPT=0
export PATH="$HOME/.poetry/bin:$PATH"
if [[ -z "$VIRTUAL_ENV" ]]; then
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
fi

export PATH="$HOME/.poetry/bin:$PATH”
```

Source your shell profile or start a new session:

```bash
source ~/<rc_file_name>
```

Verify that Poetry installed correctly:

```bash
poetry --version
```
