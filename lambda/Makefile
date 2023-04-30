#! /bin/bash

SHELL=/bin/bash
PIP=pip3
PYENV=~/.pyenv/lambda-tools/bin/activate
FUNCTION := $(shell basename $(PWD))
ZIP_PACKAGE=deployment-package.zip

FUNCTION_NAME=lambda_function


# Create virtual environment
venv: env
env: requirements.txt
	${PYENV}

# Deploy this Lambda function to AWS
deploy: install
install: env zipfile upload

zipfile: lambda_function.py
	zip ${ZIP_PACKAGE} lambda_function.py

upload:
	aws lambda update-function-code --function-name ${FUNCTION_NAME} --zip-file fileb://${ZIP_PACKAGE}

# Currently unused
#	../scripts/deploy_lambda.py --deploy --function ${FUNCTION}

clean:
	rm -rf __pycache__ *.zip

distclean:
	rm -rf deployments/deployment_* /tmp/*

deactivate:
	$(shell deactivate)

test: tests
tests:
	env
	pytest
