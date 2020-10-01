#!/bin/sh

cd /srv/fancybin

python3 manage.py collectstatic --noinput

./wait-for-it.sh postgres:5432

>&2 echo "Postgres is up, starting cores"

python3 manage.py migrate
uwsgi --socket 0.0.0.0:8001 --enable-threads --module fancybin.wsgi --processes 4
