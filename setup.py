import sys
import os
import codecs

from setuptools import setup, find_packages


__dir__ = os.path.abspath(os.path.dirname(__file__))

# To prevent a redundant __version__, import it from the packages
sys.path.insert(0, os.path.join(__dir__, 'semantics2021_toy_languages'))

try:
    from _metadata import (
        __version__, __author__, __email__, __license__, __url__,
        __description__
    )
finally:
    sys.path.pop(0)

with codecs.open(os.path.join(__dir__, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup_args = dict(
    name='semantics2021_toy_languages',

    version=__version__,

    description=__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',

    url=__url__,

    author=__author__,
    author_email=__email__,

    # license=__license__,

    classifiers=[
        # TODO
    ],
    platforms=['any'],

    keywords=[
        # TODO
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),

    install_requires=[],
    extras_require={},
    entry_points={},

    # test_suite='tests'
)


setup(**setup_args)
