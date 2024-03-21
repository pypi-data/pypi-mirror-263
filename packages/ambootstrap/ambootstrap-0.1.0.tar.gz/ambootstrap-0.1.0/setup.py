# Copyright 2024, Martijn Braam
# SPDX-License-Identifier: LGPL-3.0-only
from setuptools import setup

setup(
    name='ambootstrap',
    version='0.1.0',
    packages=['amb'],
    url='https://git.sr.ht/~martijnbraam/ambootstrap',
    license='LGPL3',
    author='Martijn Braam',
    author_email='martijn@brixit.nl',
    description='Tool for bootstrapping Alpine Linux for mobile',
    long_description=open("README.md").read(),
    classifiers=[
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: POSIX :: Linux',
    ],
    entry_points={
        'console_scripts': [
            'ambootstrap=amb.__main__:main'
        ]
    },
)
