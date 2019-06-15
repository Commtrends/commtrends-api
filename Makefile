run: .venv
	. .venv/bin/activate; APP_MODE=local python3 app.py

build: .venv

.venv: requirements.txt
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip setuptools
	.venv/bin/pip install -r requirements.txt

clean:
	rm -rf .venv