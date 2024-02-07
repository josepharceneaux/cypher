#! /bin/bash

SHELL=/bin/bash
PIP=pip3
PYENV=~/.pyenv/lambda-tools/bin/activate
FUNCTION := $(shell basename $(PWD))
ZIP_PACKAGE=../../deployment-package.zip

FUNCTION_NAME=cypher
FUNCTION_FILES=substitution.py lambda_function.py


list-functions:
	@echo "Lambda functions"
	@aws lambda list-functions | grep FunctionName

get-cypher-function:
	@echo "Cypher Function"
	@aws lambda get-function --function-name cypher

# Create virtual environment
venv: env
env: requirements.txt
	${PIP} install -r requirements.txt
	${PYENV}

deployment-package: zipfile
zipfile: clean
	mkdir package
	${PIP} install -r requirements.txt --target package
	cp ${FUNCTION_FILES} package/
	cd package
	zip -r ${ZIP_PACKAGE} .

# Currently unused
#	../scripts/deploy_lambda.py --deploy --function ${FUNCTION}


clean: distclean
distclean:
	rm -rf __pycache__ ${ZIP_PACKAGE} package
	rm -rf deployments/deployment_*

deactivate:
	$(shell deactivate)

test: tests
tests: env
	pytest
