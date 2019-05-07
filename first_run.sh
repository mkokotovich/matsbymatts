#!/bin/bash
set -xeuo pipefail

echo "Running migrations"
docker-compose exec api python manage.py migrate

echo "Restarting django"
docker-compose restart api

echo "Waiting for django to come back"
sleep 5

echo
echo "Success!"
