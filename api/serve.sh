#!/bin/bash
#flask -A main.py --debug run -h 127.0.0.1 -p 5000
gunicorn -w 2 -b 127.0.0.1:5000 'main:app'
