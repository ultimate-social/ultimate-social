echo "starting server"
python proj/manage.py migrate
python proj/manage.py runserver 0.0.0.0:8000