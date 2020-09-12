
export FLASK_APP=main.py
export FLASK_ENV=development

pipenv install -r dev-requirements.txt
pipenv install -r requirements.txt

pipenv run python main.py