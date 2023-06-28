#!/bin/bash

cythonize -3 swixknife --lenient -b -i -k
rm ../tmp* -rf
rm ../build -rf
rm ../*.so
