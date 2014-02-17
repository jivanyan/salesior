default: webserver

webserver:
	python manage.py runserver 0.0.0.0:8000

clean: cleanpython cleaneditor

cleanpython:
	find . -type f -name '*.py[cod]' -delete
	
cleaneditor:
	find . -type f -name '*.*~' -delete

systemdeps:
	sh setup/system_deps.sh

pydeps:
	pip install -e lib/django
	pip install -r setup/requirements.txt

venv:
	python3 setup/install_venv.py venv

submodules:
	git submodule update --init --recursive
