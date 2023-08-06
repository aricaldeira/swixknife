#!/bin/bash

#
# Clean compilation
#
rm dist -rf
rm build -rf
find . -type f -name "*.c" -delete

python setup.py build_ext

mkdir dist
cp build/lib.linux-x86_64-cpython-311/swixknife/swixknife -R dist/
cp swixknife/text/data/*.sor dist/swixknife/text/data/
cp swixknife/date_time/sun_moon.db dist/swixknife/date_time/

rm build -rf
find . -type f -name "*.c" -delete
