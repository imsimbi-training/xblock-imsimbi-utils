"""Set up for xblock-imsimbi-utils"""

import os
import os.path
import re
import sys
from setuptools import setup


def package_data(pkg, root_list):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for root in root_list:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    with open(filename, encoding='utf-8') as opened_file:
        version_file = opened_file.read()
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                  version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
VERSION = get_version("xblock_imsimbi_utils", "__init__.py")

print('imsimbi_util setup')
setup(
    name='xblock_imsimbi_utils',
    version=VERSION,
    description='Various utilities for XBlocks',
    long_description=README,
    author='Imsimbi',
    author_email='james@doubtful.io',
    packages=[
        'xblock_imsimbi_utils',
    ],
    install_requires=[
        'XBlock',
    ],
    # entry_points={
    #     'xblock.v1': [
    #         'xblock_imsimbi_utils = xblock_imsimbi_utils:ImsimbiUtilsXBlock',
    #     ]
    # },
    package_data=package_data("xblock_imsimbi_utils", ["public", "static", "templatetags"]),
    url='https://github.com/imsimbi-training/xblock-imsimbi-utils',
    classifiers=[
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
    ],

)
