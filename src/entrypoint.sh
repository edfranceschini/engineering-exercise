#!/bin/bash
# entrypoint.sh

CONTAINER_ALREADY_STARTED="CONTAINER_ALREADY_STARTED_PLACEHOLDER"
if [ ! -e $CONTAINER_ALREADY_STARTED ]; then
    # First time the container starts, load initial data
    # Not the more elegant solution, but it works
    touch $CONTAINER_ALREADY_STARTED
    echo "-- First container startup --"
    flask db init
    flask db migrate
    flask db upgrade
    python load_initial_data.py

else
    echo "-- Not first container startup --"
fi

gunicorn -w 4 -b :8000 wsgi:app