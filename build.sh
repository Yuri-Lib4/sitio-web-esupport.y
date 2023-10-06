#!/usr/bin/env bash
# exit on error
set -o errexit
cd /support/support

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
