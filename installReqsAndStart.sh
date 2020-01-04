#!/bin/bash

MD5=$(md5sum .requirements.txt | cut -f1 -d' ')
if ! [ -d ".data/$MD5-site-packages" ]; then
    rm -rf .data/*-site-packages
    pip3 install -U -r .requirements.txt -t ".data/$MD5-site-packages"
fi
exec env PYTHONPATH="$PWD/.data/$MD5-site-packages" gunicorn -b "0.0.0.0:5000" -w 4 webapp:app

