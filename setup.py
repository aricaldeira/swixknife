

from setuptools import setup, find_packages
# from Cython.Build import cythonize
import swixknife

packages = find_packages()
modules = [pack.replace('.', '/') + '/*.py' for pack in packages]

setup(
    name='swixknife',
    version=swixknife.__version__,
    packages=packages,
    package_data={
        '': [
            '*.sor',
            'sun_moon.db',
        ]
    },
    # ext_modules=cythonize(
    #     module_list=modules,
    #     language_level='3',
    # )
)
