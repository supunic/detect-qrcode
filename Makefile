.PHONY: setup-mac
setup-mac:
	python -m venv venv --clear 
	venv/bin/pip install -r requirements.txt