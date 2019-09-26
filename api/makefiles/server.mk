server.install:
	pip install -r requirements-dev.txt --user --upgrade --no-warn-script-location

server.start:
	python src/server.py

server.logs:
	tail -f server.log

server.upgrade:
	pip-upgrade requirements.txt requirements-dev.txt --skip-virtualenv-check
