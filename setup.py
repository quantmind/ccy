import os

from setuptools import find_packages, setup

import ccy


def read(name):
    filename = os.path.join(os.path.dirname(__file__), name)
    with open(filename, encoding="utf8") as fp:
        return fp.read()


def requirements(name):
    install_requires = []
    dependency_links = []

    for line in read(name).split("\n"):
        if line.startswith("-e "):
            link = line[3:].strip()
            if link == ".":
                continue
            dependency_links.append(link)
            line = link.split("=")[1]
        line = line.strip()
        if line:
            install_requires.append(line)

    return install_requires, dependency_links


install_requires = requirements("dev/requirements.txt")[0]
tests_require = requirements("dev/requirements-dev.txt")[0]


meta = dict(
    name="ccy",
    version=ccy.__version__,
    description=ccy.__doc__,
    author="Luca Sbardella",
    author_email="luca@quantmind.com",
    maintainer_email="luca@quantmind.com",
    url="https://github.com/quantmind/ccy",
    license="BSD",
    long_description=read("README.rst"),
    packages=find_packages(include=["ccy", "ccy.*"]),
    install_requires=install_requires,
    tests_require=tests_require,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Office/Business :: Financial",
        "Topic :: Utilities",
    ],
)


if __name__ == "__main__":
    setup(**meta)
