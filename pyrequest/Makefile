VENV = venv
PYTHON = $(VENV)/Scripts/python
PIP = $(VENV)/Scripts/pip

$(VENV)/Scripts/activate: requirements.txt
	python -m venv $(VENV)
	$(PIP) install -r requirements.txt

run: $(VENV)/Scripts/activate
	$(PYTHON) main.py

clean:
	rm -rf __pycache__
	rm -rf venv

# rollback add command
gitundoadd:
	git reset