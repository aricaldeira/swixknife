#!/bin/bash

cython sun_moon_ephem.py --embed -3
gcc -Os -I /usr/include/python3.11 -o sun_moon_ephem sun_moon_ephem.c -lpython3.11 -lpthread -lm -lutil -ldl
