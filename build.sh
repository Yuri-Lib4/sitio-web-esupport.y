#!/usr/bin/env bash
# exit on error
set -o errexit


# Directorio de trabajo de Render
RENDER_WORKING_DIR=supporte

# Cambia al directorio de trabajo de Render
cd $RENDER_WORKING_DIR
# Instala las dependencias desde requirements.txt si existe
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "El archivo requirements.txt no se encontró en la ubicación especificada.."
    exit 1
fi

rm db.sqlite3
rm -r esupport/migrations
python manage.py collectstatic --no-input

python manage.py migrate
