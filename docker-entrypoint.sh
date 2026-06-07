#!/bin/sh
set -e
uv run manage.py migrate
uv run manage.py load_sample_data
uv run gunicorn task_tracker.wsgi --bind=:8000

