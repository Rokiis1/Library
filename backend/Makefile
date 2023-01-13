install:
		#install commands
		pip install --upgrade pip &&\
			pip install -r requirements.txt
format:
		#format code
		black *.py database/*.py services/*.py routes/*.py models/*.py
lint:
		#flake8 or #pylint
		pylint --disable=R,C *.py database/*.py services/*.py routes/*.py models/*.py