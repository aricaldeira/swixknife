#!/bin/bash

#
# Clean compilation
#
find . -type f -name "*.cpython-311-x86_64-linux-gnu.so" -delete
find . -type f -name "*.c" -delete
rm build -rf

python setup.py build_ext

mkdir dist
cp build/lib.linux-x86_64-cpython-311/swixknife -R dist/
cp swixknife/text/data/*.sor dist/swixknife/text/data/
cp swixknife/date_time/sun_moon.db dist/swixknife/date_time/
rm build -rf
