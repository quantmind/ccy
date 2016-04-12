import os
from setuptools import setup, find_packages

import config

b = os.path.dirname(__file__)

meta = dict(
    name='ccy',
    author='Luca Sbardella',
    author_email="luca@quantmind.com",
    maintainer_email="luca@quantmind.com",
    url="https://github.com/lsbardel/ccy",
    license="BSD",
    long_description=config.read(os.path.join(b, 'README.rst')),
    packages=find_packages(include=['ccy', 'ccy.*']),
    install_requires=config.requirements(os.path.join(b, 'requirements.txt')),
    zip_safe=False,
    test_suite="tests.suite",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Office/Business :: Financial',
        'Topic :: Utilities'
    ]
)


if __name__ == '__main__':
    setup(**config.setup(meta, 'ccy'))
