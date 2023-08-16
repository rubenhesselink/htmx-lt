make first_run:
	python -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
	python manage.py migrate
	python manage.py runserver

make run:
	source venv/bin/activate
	python manage.py migrate
	python manage.py runserver