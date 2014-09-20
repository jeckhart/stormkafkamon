#!/usr/bin/env python

import setuptools

install_requires = [
    'PrettyTable==0.7.2',
    'kazoo>=2.0',
    'simplejson',
    'argparse',
    'requests',
    'kafka-python>=0.9.0'
]

setuptools.setup(
    name = 'stormkafkamon',
    version = '0.2.0',
    license = 'Apache',
    description = '''Monitor offsets of a storm kafka spout.''',
    author = "Philip O'Toole",
    author_email = 'philipomailbox-github@yahoo.com',
    url = 'https://github.com/otoolep/stormkafkamon',
    platforms = 'any',
    packages = ['stormkafkamon'],
    zip_safe = True,
    verbose = False,
    install_requires = install_requires,
    dependency_links = ['https://github.com/mumrah/kafka-python/tarball/0.7#egg=kafka-python-0.7.2-0'],
    entry_points={
        'console_scripts': [
            'skmon = stormkafkamon.monitor:main'
        ]
    },
)
