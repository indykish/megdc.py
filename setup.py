from setuptools import setup, find_packages
import os
import sys
import megdc 


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    f = open(path)
    return f.read()

install_requires = []
pyversion = sys.version_info[:2]
if pyversion < (2, 7) or (3, 0) <= pyversion <= (3, 1):
    install_requires.append('argparse')

#
# Add libraries that are not part of install_requires but only if we really
# want to, specified by the environment flag
#

setup(
    name='megdc',
    version=megdc.__version__,
    packages=find_packages(),

    author='Megam system team',
    author_email='support@megam.io',
    description='Deploy megam with minimal infrastructure',
    long_description=read('README.rst'),
    license='MEGAM SYSTEM',
    keywords='megdc',
    url="https://github.com/megamsys/megdc",

    install_requires=[
        'setuptools',
        ] + install_requires,

    tests_require=[
        'pytest >=2.1.3',
        'mock >=1.0b1',
        ],

    entry_points={

        'console_scripts': [
            'megdc = megdc.cib:main',
            ],

        'megdc.cib': [
            'install = megdc.install:make',
            'uninstall = megdc.install:make_uninstall',
            ],

        },
    )
