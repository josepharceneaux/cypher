#! /bin/bash

SHELL=/bin/bash
PIP=pip3
PYENV=~/.pyenv/lambda-tools/bin/activate
FUNCTION := $(shell basename $(PWD))
ZIP_PACKAGE=deployment-package.zip

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
	${PYENV}

# Deploy this Lambda function to AWS
deploy: install
install: env zipfile upload

zipfile: clean
	zip ${ZIP_PACKAGE} ${FUNCTION_FILES}

upload:
	aws lambda update-function-code --function-name ${FUNCTION_NAME} --zip-file fileb://${ZIP_PACKAGE}

# Currently unused
#	../scripts/deploy_lambda.py --deploy --function ${FUNCTION}

clean:
	rm -rf __pycache__ ${ZIP_PACKAGE}

distclean:
	rm -rf deployments/deployment_* /tmp/*

deactivate:
	$(shell deactivate)

test: tests
tests:
	${PIP} install -r requirements.txt
#	env
	pytest
