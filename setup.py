

from setuptools import setup, find_packages
import swixknife


setup(
    name = 'swixknife',
    version = swixknife.__version__,
    packages = find_packages(),
    package_data={'': ['*.sor']}
)
