#!/bin/bash

#
# Clean compilation
#
find . -type f -name "*.cpython-311-x86_64-linux-gnu.so" -delete
find . -type f -name "*.c" -delete
rm build -rf

python setup.py build

cp swixknife/text/data/*.sor build/lib.linux-x86_64-cpython-311/swixknife/swixknife/text/data/
cp swixknife/date_time/sun_moon.db build/lib.linux-x86_64-cpython-311/swixknife/swixknife/date_time/
