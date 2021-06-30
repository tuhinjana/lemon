#!/usr/bin/env bash
echo 'Your container args are:' ${ENV}

python manage.py makemigrations
python manage.py migrate orders
python manage.py collectstatic --noinput
if [[ -z "${ENV}" ]]; then
    python3.9 manage.py runserver 0.0.0.0:8000
else
    echo "run test"
    python3.9 -u manage.py test orders.tests --noinput | tee 2>&1
fi;
#tail -f /dev/null
