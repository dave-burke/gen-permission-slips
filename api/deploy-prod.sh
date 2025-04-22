#!/bin/sh

set -e

TARGET=${1}
APP_NAME=camp-forms

# Build container
docker build -t ${APP_NAME} .
docker save -o ${APP_NAME}.tar ${APP_NAME}:latest

# Copy files to remote host
rsync --progress ./${APP_NAME}.tar ${TARGET}:
rsync -v ./${APP_NAME}-labels.txt ${TARGET}:

# Load and start the container
/bin/ssh ${TARGET} docker load -i ${APP_NAME}.tar
/bin/ssh ${TARGET} docker rm -f ${APP_NAME}
/bin/ssh ${TARGET} docker run -d --label-file ./${APP_NAME}-labels.txt --name ${APP_NAME} ${APP_NAME}:latest

# Clean up
rm -v ${APP_NAME}.tar
# /bin/ssh ${TARGET} rm -v ${APP_NAME}.tar ${APP_NAME}-labels.txt

