# Makefile for Lambda cypher function

# Lambda targets
BUCKET_NAME=arceneaux.me
BUCKET_URI=s3://${BUCKET_NAME}

# Local places
LOCAL_STATIC_DIR=~/src/web/cypher


all:
	@echo "Making all"
	install-static

list-buckets:
	@echo "S3 buckets"
	@aws s3 ls

list-functions:
	@echo "All Lambda functions"
	@aws lambda list-functions | grep FunctionName

static: install-static
install-static:
	@echo "Uploading static files"
	@aws s3 cp ./cypher.html ${BUCKET_URI}/cypher.html
	@aws s3api put-object-acl --bucket ${BUCKET_NAME} --key cypher.html --acl public-read
	@aws s3 cp ./index.html ${BUCKET_URI}/index.html
	@aws s3api put-object-acl --bucket ${BUCKET_NAME} --key index.html --acl public-read
	@aws s3 cp ./index.css ${BUCKET_URI}/index.css
	@aws s3api put-object-acl --bucket ${BUCKET_NAME} --key index.css --acl public-read

# If we want to istall stuff locally
# install-local-static:
# 	@echo "Copying LOCAL static files"
# 	@cp ./cypher.html ${LOCAL_STATIC_DIR}/

function-zip-file: deployment-package.zip
deployment-package.zip:
	zip deployment-package.zip subsitutionn.py lambda_function.py

install-lambda:
	@echo "Uploading Lambda function"

install: install-static install-lambda

clean:
	rm -f *~
