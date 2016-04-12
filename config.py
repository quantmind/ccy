"""Configuration for test and setup.py utilities"""
import os
import sys
import json
import subprocess


docs_bucket = 'quantmind-docs'


def setup(params, package=None):
    if package:
        path = os.path.abspath(os.getcwd())
        meta = sh('%s %s package_info %s %s'
                  % (sys.executable, __file__, package, path))
        params.update(json.loads(meta))

    return params


def read(name):
    with open(name) as fp:
        return fp.read()


def requirements(name):
    install_requires = []
    dependency_links = []

    for line in read(name).split('\n'):
        if line.startswith('-e '):
            link = line[3:].strip()
            if link == '.':
                continue
            dependency_links.append(link)
            line = link.split('=')[1]
        line = line.strip()
        if line:
            install_requires.append(line)

    return install_requires, dependency_links


def sh(command):
    return subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True,
                            universal_newlines=True).communicate()[0]


if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[1] == 'package_info':
        package = sys.argv[2]
        if len(sys.argv) > 3:
            sys.path.append(sys.argv[3])
        pkg = __import__(package)
        print(json.dumps(dict(version=pkg.__version__,
                              description=pkg.__doc__)))
    else:
        from agile import AgileManager

        AgileManager(description='Release manager for ccy').start()
