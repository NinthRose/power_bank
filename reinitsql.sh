

find | grep migrations | grep 000 | xargs rm

python manage.py makemigrations

python manage.py migrate

