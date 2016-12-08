rm db.sqlite3
rm -rf frijay/migrations/
mkdir frijay/migrations/
touch frijay/migrations/__init__.py
python manage.py makemigrations
python manage.py migrate
#Default admin credentials:
echo "from django.contrib.auth.models import User; User.objects.create_superuser('frijay', '', 'frijay_pass')" | python manage.py shell
python manage.py populate_db

