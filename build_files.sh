pip install -r requirements.txt
python3.12 manage.py collectstatic --noinput
python3.12 manage.py makemigration --noinput
python3.12 manage.py migrate --noinput