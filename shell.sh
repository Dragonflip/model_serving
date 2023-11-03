#! /bin/sh

python download_model.py
python manage.py makemigrations
python maange.py migrate
python manage.py runserver 0.0.0.0:8000

