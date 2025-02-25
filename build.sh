#!/bin/bash

echo "BUILD START"
python3.12 -m ensurepip
python3.12 -m pip install -r requirements.txt
echo "BUILD END"

python3.12 manage.py migrate

echo "Collect Static..."
python3.12 manage.py collectstatic