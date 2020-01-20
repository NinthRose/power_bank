

find | grep migrations | grep 000 | xargs rm
rm sql.db

python manage.py makemigrations

python manage.py migrate

