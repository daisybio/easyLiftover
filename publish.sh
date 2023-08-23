#!/bin/bash

poetry run pytest && \
    poetry build && \
    poetry publish