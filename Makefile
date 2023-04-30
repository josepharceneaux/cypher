# Makefile for Lambda cypher function

BUCKET_NAME=arceneaux.me
BUCKET_URI=s3://${BUCKET_NAME}

all:
	@echo "Making all"

list-buckets:
	@echo "S3 buckets"
	@aws s3 ls

install-static:
	@echo "Uploading static files"
	@aws s3 cp ./cypher.html ${BUCKET}/cypher.html
	@aws s3api put-object-acl --bucket ${BUCKET_NAME} --key cypher.html --acl public-read
	@aws s3 cp ./index.html ${BUCKET}/index.html
	@aws s3api put-object-acl --bucket ${BUCKET_NAME} --key index.html --acl public-read

install-lambda:
	@echo "Uploading Lambda function"

install: install-static install-lambda

clean:
	rm *~