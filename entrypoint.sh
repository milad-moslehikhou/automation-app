#!/bin/sh

if [[ "$1" == "startcelery" ]] ; then
    celery -A automation_app worker -l INFO
    shift
elif [[ "$1" == "startgunicorn" ]] ; then
    until nc -z -w30 $DB_HOST $DB_PORT ; do
        echo "Waiting for database connection, try after 1 second..."
        sleep 1
    done

    if [[ -z $(find static/ -type f) ]] ; then
    	python manage.py collectstatic --noinput
    fi
    python manage.py migrate
    cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.filter(username='$DJANGO_ADMIN_USER').exists() or User.objects.create_superuser('$DJANGO_ADMIN_USER', '', '$DJANGO_ADMIN_PASS')
EOF
    gunicorn automation_app.wsgi:application --bind 0.0.0.0:8000
    shift
fi

exec "$@"
