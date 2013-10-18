import sys


def ispy3k():
    return int(sys.version[0]) >= 3


if ispy3k():
    string_type = str
    itervalues = lambda d: d.values()
    iteritems = lambda d: d.items()
    is_string = lambda x: isinstance(x, str)
    from io import StringIO
else:  # Python 2    # pragma nocover
    string_type = unicode
    itervalues = lambda d: d.itervalues()
    iteritems = lambda d: d.iteritems()
    is_string = lambda x: isinstance(x, basestring)
    from cStringIO import StringIO
