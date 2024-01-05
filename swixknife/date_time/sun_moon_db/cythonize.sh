#!/bin/bash

cython sun_moon_astronomy.py --embed -3
gcc -Os -I /usr/include/python3.11 -o sun_moon_astronomy sun_moon_astronomy.c -lpython3.11 -lpthread -lm -lutil -ldl

cython solstices_equinoxes.py --embed -3
gcc -Os -I /usr/include/python3.11 -o solstices_equinoxes solstices_equinoxes.c -lpython3.11 -lpthread -lm -lutil -ldl
