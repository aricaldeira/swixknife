#!/bin/bash

#
# Clean compilation
#
find . -type f -name "*.cpython-311-x86_64-linux-gnu.so" -delete
find . -type f -name "*.c" -delete

#cythonize -3 swixknife --lenient -b -i -k
