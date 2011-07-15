# Makefile
.PHONY : dependencies check test

test: dependencies
	bash -c 'source testenv/bin/activate; python manage.py test'

dependencies:
	virtualenv testenv
	pip -q install -E testenv -r requirements.txt

check: dependencies
	@echo "-----------------"
	@echo "    pylinting    "
	@echo "-----------------"
	bash ../makesupport.sh

	@echo "-----------------"
	@echo "    pep8'ing     "
	@echo "-----------------"
	pep8 --repeat --ignore=E501 *.py
