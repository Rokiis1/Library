install:
		#install commands
		pip3 install --upgrade pip &&\
			pip3 install -r requirements.txt
format:
		#format code
		black *.py database/*.py services/*.py routes/*.py models/*.py
lint:
		#flake8 or #pylint
		pylint --disable=R,C *.py database/*.py services/*.py routes/*.py models/*.py