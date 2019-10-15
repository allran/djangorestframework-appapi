#!/usr/bin/env python
from __future__ import print_function

import os
import re
import sys

from setuptools import setup


def read(*paths):
    """
    Build a file path from paths and return the contents.
    """
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


if sys.argv[-1] == 'publish':
    # os.system("python setup.py sdist upload")
    # os.system("python setup.py bdist_wheel upload")
    os.system("python3 setup.py sdist bdist_wheel")
    os.system("twine check dist/*")
    os.system("twine upload dist/*")
    # os.system("python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* --verbose")
    print("You probably want to also tag the version now:")
    print("  git tag -a {0} -m 'version {0}'".format(
        get_version('rest_framework_app_api')))
    print("  git push --tags")
    sys.exit()

setup(
    name='djangorestframework-appapi',
    version=get_version('rest_framework_app_api'),
    url='https://github.com/allran/djangorestframework-appapi',
    license='BSD',
    description='A Django REST framework API adapter for the App(IOS, Andorid, WebApp) API spec.',
    long_description=read('README.rst'),
    long_description_content_type='text/x-rst',
    author='Allran.Qu',
    author_email='',
    packages=get_packages('rest_framework_app_api'),
    package_data=get_package_data('rest_framework_app_api'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'djangorestframework>=3.10',
        'django>=1.11',
    ],
    extras_require={

    },
    python_requires=">=3.5",
    zip_safe=False,
)
