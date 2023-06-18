#!/bin/bash

CERT_FILE=$1
KEY_FILE=$2


if [[ -z "$CERT_FILE" && -z "$KEY_FILE" ]]
then
    gunicorn --bind "127.0.0.1:8000" webuplift.wsgi:application
else
    gunicorn --bind "0.0.0.0:443" --certfile=$CERT_FILE --keyfile=$KEY_FILE webuplift.wsgi:application
fi