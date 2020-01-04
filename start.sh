#!/usr/bin/env bash

set -o errexit
set -o nounset

pip3 install -r requirements.txt
python3 webapp.py
