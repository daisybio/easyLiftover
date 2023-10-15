#!/bin/bash

poetry build && \
    poetry publish && \
    docker build . -t bigdatainbiomedicine/easyliftover && \
    docker push bigdatainbiomedicine/easyliftover