#!/usr/bin/env bash

set -o errexit
set -o nounset

pip3 install -r --user requirements.txt
gunicorn -b "0.0.0.0:5000" -w 4 webapp:app
