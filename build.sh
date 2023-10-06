#!/usr/bin/env bash
# exit on error
set -o errexit


# Directorio de trabajo de Render
RENDER_WORKING_DIR=sitio-web-esupport/support

# Cambia al directorio de trabajo de Render
cd $RENDER_WORKING_DIR
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
