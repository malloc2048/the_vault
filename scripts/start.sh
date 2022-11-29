#!/usr/bin/env bash

gunicorn -c app/config/gunicorn.conf.py app:app
