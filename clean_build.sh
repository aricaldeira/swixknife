#!/bin/bash

rm dist -rf
rm build -rf
rm swixknife.egg-info -rf

python setup.py clean
python setup.py bdist_wheel
cp dist/*.whl docs/static/python/

rm swixknife.egg-info -rf
# rm build -rf
#rm dist -rf
