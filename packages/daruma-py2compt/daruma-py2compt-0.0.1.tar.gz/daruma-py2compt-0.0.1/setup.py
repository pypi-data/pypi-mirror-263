import sys
from setuptools import setup, find_packages


python_version = sys.version_info
if python_version < (2, 4):
    raise ValueError("This package does not support Python versions less than 2.4 or between 3.0 and 3.1.")
elif python_version < (3, 0):
    install_package = 'daruma-py2compt'
elif python_version < (3, 1):
    raise ValueError("This package does not support Python versions less than 2.4 or between 3.0 and 3.1.")
elif python_version >= (3, 1):
    install_package = 'daruma'


setup(
    name=install_package,
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'daruma=daruma_py2compt.daruma_module:main',
        ],
    },
    install_requires=[
        'numpy==1.16.6; python_version <= "2.7"', 
        'numpy>=1.19.2; python_version >= "3.1"',
    ],
    include_package_data=True,
    package_data={'daruma_py2compt': ['daruma_py2compt/data/AAindex553-Normal-X0.feature','daruma_py2compt/data/CV5.weight']},
)

