install:
		#install commands
		pip3 install --upgrade pip &&\
			pip3 install -r requirements.txt
format:
		#format code
		black *.py database/*.py services/*.py routes/*.py models/*.py
lint:
		#flake8 or #pylint
		pylint --disable=R,C services/*.py database/*.py routes/*.py
test:
		#test
		python -m pytest -vv test/test_database_manager.py test/test_main.py
build:
		#build container
		docker build -t rokiis1/backend-library .