.DEFAULT_GOAL := all
RESULT_FILE="results.txt"

all: install test run deploy

install:
  @echo "Installing pipenv enviroment."
  pipenv --python 3.8
  pipenv install requests
  pipenv install ntplib
  pipenv install pytest

test:
  @echo "Start tests..."
  pipenv run pytest tests/tests.py > results.txt

run:
  @echo "Run Python app..."
  pipenv run python3 app.py >> results.txt

deploy:
  @echo "Deploying results.txt to Git."
  git add results.txt
  git commit
  git push origin main
