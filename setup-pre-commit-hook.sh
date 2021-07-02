#!/bin/bash
#
# Install a git pre-commit hook to format and lint Python files
#
# See https://rikwatson.github.io/python_lint for more details
#
echo $'#/bin/sh\nblack .\npython lint.py -p ./sampleProject'> .git/hooks/pre-commit

chmod +x .git/hooks/pre-commit
