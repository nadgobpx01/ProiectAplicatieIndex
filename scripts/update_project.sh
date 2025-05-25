#!/bin/bash
cd /opt/django_app
git fetch origin main
git reset --hard origin/main
git clean -fd
docker exec index_app python manage.py migrate || true
docker exec index_app python manage.py collectstatic --noinput || true
docker restart index_app || true