.PHONY: run init test train

init:
	python -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

migrate:
	. .venv/bin/activate && python manage.py migrate

train:
	. .venv/bin/activate && python app/ml/train_model.py

run:
	. .venv/bin/activate && python manage.py runserver 0.0.0.0:8000

test:
	. .venv/bin/activate && pytest -q
