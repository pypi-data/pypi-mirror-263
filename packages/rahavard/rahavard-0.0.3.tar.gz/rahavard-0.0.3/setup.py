from os import path
from setuptools import setup, find_packages

import codecs


here = path.abspath(path.dirname(__file__))
with codecs.open(path.join(here, 'README.md'), encoding='utf-8') as fh:
    long_description = '\n' + fh.read()


VERSION = '0.0.3'
DESCRIPTION = 'Re-Usable Utils'
LONG_DESCRIPTION = 'Re-Usable Utils to Be Used on Our Django Projects'

setup(
    name='rahavard',
    version=VERSION,
    author='Davoud Arsalani',
    author_email='d_arsalani@yahoo.com>',
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'convert_numbers',
        'jdatetime',
        'natsort',
    ],
    keywords=['python',],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ]
)
