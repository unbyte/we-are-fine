#!/bin/sh
echo 'initialize database' && \
python ./init-database.py && \
echo 'init successfully' && \
echo 'start server' && \
python ./run-production.py