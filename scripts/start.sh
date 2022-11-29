#!/usr/bin/env bash

gunicorn -c app/gunicorn.conf.py app:app
