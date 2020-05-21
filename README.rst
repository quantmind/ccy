A python module for currencies. The module compiles a dictionary of
currency objects containing information useful in financial analysis.
Not all currencies in the world are supported yet. You are welcome to
join and add more.

:Package: |version| |license| |pyversions| |status| |downloads|
:CI: |master-build| |coverage-master|
:Dowloads: https://pypi.org/project/ccy/
:Source: https://github.com/quantmind/ccy

.. |version| image:: https://badge.fury.io/py/ccy.svg
  :target: https://badge.fury.io/py/ccy
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/ccy.svg
  :target: https://pypi.org/project/ccy/
.. |license| image:: https://img.shields.io/pypi/l/ccy.svg
  :target: https://pypi.org/project/ccy/
.. |status| image:: https://img.shields.io/pypi/status/ccy.svg
  :target: https://pypi.org/project/ccy/
.. |downloads| image:: https://img.shields.io/pypi/dd/ccy.svg
  :target: https://pypi.org/project/ccy/
.. |master-build| image:: https://github.com/quantmind/ccy/workflows/build/badge.svg
  :target: https://github.com/quantmind/ccy/actions?query=workflow%3Abuild
.. |coverage-master| image:: https://codecov.io/gh/quantmind/ccy/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/quantmind/ccy


.. contents::
    :local:


Currency object
======================
To use it::

    >>> import ccy
    >>> c = ccy.currency('aud')
    >>> c.printinfo()
    code: AUD
    twoletterscode: AD
    rounding: 4
    default_country: AU
    isonumber: 036
    order: 3
    name: Australian Dollar
    >>> c.as_cross()
    'AUDUSD'
    >>> c.as_cross('/')
    'AUD/USD'

a currency object has the following properties:

* *code*: the `ISO 4217`_ code.
* *twoletterscode*: two letter code (can't remeber the ISO number). Very useful for financial data providers such as Bloomberg.
* *default_country*: the default `ISO 3166-1 alpha-2`_ country code for the currency.
* *isonumber*: the ISO 4217 number.
* *name*: the name of the currency.
* *order*: default ordering in currency pairs (more of this below).
* *rounding*: number of decimal places

Currency Crosses
~~~~~~~~~~~~~~~~~~~~~~~~~~

You can create currency pairs by using the ``currency_pair`` function::

    >>> import ccy
    >>> p = ccy.currency_pair('eurusd')
    >>> p
    ccy_pair: EURUSD
    >>> p.mkt()  # market convention pair
    ccy_pair: EURUSD
    >>> p = ccy.currency_pair('chfusd')
    >>> p
    ccy_pair: CHFUSD
    >>> p.mkt()  # market convention pair
    ccy_pair: USDCHF


Some shortcuts::

    >>> import ccy
    >>> ccy.cross('aud')
    'AUDUSD'
    >>> ccy.crossover('eur')
    'EUR/USD'
    >>> ccy.crossover('chf')
    'USD/CHF'

Note, the Swiss franc cross is represented as 'USD/CHF', while the Aussie Dollar
and Euro crosses are represented with the USD as denominator.
This is the market convention which is handled by the **order** property
of a currency object.

Country information
~~~~~~~~~~~~~~~~~~~~~~~~~~

To use it::

    >>> import ccy
    >>> c = ccy.country('us')
    >>> c
    'United States'
    >>> ccy.countryccy('us')
    'USD'


Not all the country codes are standard `ISO 3166-1 alpha-2`_.
There is a function for adding extra pseudo-countries::

    import ccy
    ccy.set_new_country('EU','EUR','Eurozone')

Set a new country with code 'EU', currency 'EUR' named 'Eurozone'.
This pseudo country is set in the library already.

Countries
==============

Country information is obtained via the pytz_ package which is strict
requirement for ``ccy``::

    >>> from ccy import country
    >>> country('it')
    'Italy'

It knows about the 18 eurozone_ countries (European countries which share the
euro as common currency)::

    >>> from ccy import eurozone

eurozone is tuple of country ISO codes::

    >>> import ccy
    >>> ccy.print_eurozone()
    Austria
    Belgium
    Cyprus
    Estonia
    Finland
    France
    Germany
    Greece
    Ireland
    Italy
    Latvia
    Lithuania
    Luxembourg
    Malta
    Netherlands
    Portugal
    Slovakia
    Slovenia
    Spain


Date and Periods
===================

The module is shipped with a ``date`` module for manipulating time periods and
converting dates between different formats. The *period* function can be used
to create ``Period`` instances::

    >>> from ccy import period
    >>> p = period('1m')
    >>> p
    1M
    >>> p += '2w'
    >>> p
    1M2W
    >>> P += '3m'
    >>> p
    4M2W


Installation
================
This library works for Python 2.6 and higher, including Python 3.
In addition, it requires:

* pytz_ for Countries information.
* dateutils_ for date calculations

Install using ``pip``::

    pip install ccy

or from source::

    python setup.py install


Runnung tests
~~~~~~~~~~~~~~~~~~~~~

From within the package directory::

    python setup.py test


.. _pytz: http://pytz.sourceforge.net/
.. _`ISO 3166-1 alpha-2`: http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
.. _`ISO 4217`: http://en.wikipedia.org/wiki/ISO_4217
.. _dateutils: https://pypi.python.org/pypi/python-dateutil
.. _eurozone: http://www.eurozone.europa.eu/euro-area/euro-area-member-states/
