#!/bin/bash

rm dist -rf
rm build -rf
rm swixknife.egg-info -rf

python setup.py clean
python setup.py bdist_wheel
cp dist/*.whl docs/static/python/

#
# Clean compilation
#
find . -type f -name "*.py[co]" -delete
find . -type d -name "__pycache__" -delete
find . -type f -name "*.py~" -delete
rm swixknife.egg-info -rf

rm build -rf
# rm dist -rf
