#!/bin/zsh

VENV_PY="$(pwd)/.venv/bin/python"

CURRENT_PY="$(command -v python)"

if [[ "$CURRENT_PY" != "$VENV_PY" ]]; then
    echo "activate the fucking venv dumbass"
else
    "$VENV_PY" "$(pwd)/main.py"
fi