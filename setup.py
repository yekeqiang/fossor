# Copyright 2017 LinkedIn Corporation. All rights reserved. Licensed under the BSD-2 Clause license.
# See LICENSE in the project root for license information.

import io

from setuptools import setup, find_packages


description = 'A plugin oriented tool for automating the investigation of broken hosts and services.'
try:
    with io.open('README.md', encoding="utf-8") as fh:
            long_description = fh.read()
except IOError:
    long_description = description

setup(
    name='fossor',
    version='0.0.1',
    description=description,
    long_description=description,
    # url='https://github.com/linkedin/fossor',
    author='LinkedIn',
    author_email='scallist@linkedin.com',
    license='License :: OSI Approved :: BSD License',
    packages=find_packages(),
    install_requires=[
        'flake8==3.5.0',
        'click==6.7',
        'psutil==5.4.1',
        'pytest-timeout==1.2.0',
        'setproctitle==1.1.10',
        'requests==2.18.4',
        'mock==2.0.0',
        'humanfriendly==4.4.1',
        'parsedatetime==2.4',
        'PTable==0.9.2',
    ],
    tests_require=[
        'pytest==3.0.6',
    ],
    entry_points={
        'console_scripts': [
            'fossor = fossor.cli:main',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: POSIX :: Linux'
    ]
)