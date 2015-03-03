import os
import sys

from setuptools import setup

os.environ['ccy_setup_running'] = 'yes'


package_name = 'ccy'
root_dir = os.path.dirname(__file__)
package_dir = os.path.join(root_dir, package_name)


def get_module():
    if root_dir not in sys.path:
        sys.path.insert(0, root_dir)
    return __import__(package_name)


mod = get_module()


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def requirements():
    try:
        req = read('requirements.txt').split('\n')
        result = []
        for r in req:
            r = r.replace(' ', '')
            if r:
                result.append(r)
        return result
    except:
        return []


def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)


# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
def get_rel_dir(d, base, res=''):
    if d == base:
        return res
    br, r = os.path.split(d)
    if res:
        r = os.path.join(r, res)
    return get_rel_dir(br, base, r)


packages = []
pieces = fullsplit(root_dir)
if pieces[-1] == '':
    len_root_dir = len(pieces) - 1
else:
    len_root_dir = len(pieces)

for dirpath, dirnames, filenames in os.walk(package_dir):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        packages.append('.'.join(fullsplit(dirpath)[len_root_dir:]))


setup(
    name=package_name,
    version=mod.__version__,
    author=mod.__author__,
    author_email=mod.__contact__,
    url=mod.__homepage__,
    license=mod.__license__,
    description=mod.__doc__,
    long_description=read('README.rst'),
    packages=packages,
    package_dir={'ccy': 'ccy'},
    install_requires=requirements(),
    zip_safe=False,
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
        'Topic :: Office/Business :: Financial',
        'Topic :: Utilities'
    ],
)
