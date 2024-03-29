# Makefile for Lambda cypher function

# Lambda targets
BUCKET_NAME=arceneaux.me
BUCKET_URI=s3://${BUCKET_NAME}
FUNCTION_NAME=cypher

# Local places
LOCAL_STATIC_DIR=~/src/web/cypher


all:
	@echo "Making all"
	install-static

list-buckets:
	@echo "S3 buckets"
	@aws s3 ls

list-arceneaux:
	@echo "Arceneaux.me contents"
	@aws s3 ls arceneaux

list-functions:
	@echo "All Lambda functions"
	@aws lambda list-functions | grep FunctionName

describe-function:
	@echo "Function ${FUNCTION_NAME}"
	@aws lambda get-function --function-name ${FUNCTION_NAME}

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
# 	2@echo "Copying LOCAL static files"
# 	@cp ./cypher.html ${LOCAL_STATIC_DIR}/


deployment-package.zip:
	@echo "Making lambda function"
	cd lambda
	make deployment-package.zip

install-lambda: deployment-package.zip
	@echo "Uploading Lambda function"
	@aws s3api put-object-acl --bucket ${BUCKET_NAME} --key deployment-package.zip --acl public-read
	@aws s3 cp ./lambda/deployment-package.zip ${BUCKET_URI}/deployment-package.zip

install: install-static install-lambda

tests: test
test:
	cd lambda; make test

clean:
	rm -f *~
	cd lambda; make clean
