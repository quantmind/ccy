===========
ccy
===========

Python module for currencies. The module compiles a dictionary of
currency objects containing information useful in financial analysis.

Not all currencies in the world are supported yet.
You are welcome to join and add more.


.. contents::
    :local:
    
  
Currency object
======================
To use it::

    >>> import ccy
    >>> c = ccy.currency('aud')
    >>> c.printinfo()
    code: AUD
    twolettercode: AD
    roundoff: 4
    default_country: AU
    isonumber: 036
    order: 3
    name: Australian Dollar
    >>> c.as_cross()
    'AUDUSD'
    >>> c.as_cross('/')
    'AUD/USD'

a currency object has the following properties:

* *code*: the [http://en.wikipedia.org/wiki/ISO_4217 ISO 4217] code.
* *twolettercode*: two letter code (can't remeber the ISO number). Very useful for financial data providers such as Bloomberg.
* *default_country*: the default `ISO 3166-1 alpha-2`_ country code for the currency.
* *isonumber*: the ISO 4217 number.
* *name*: the name of the currency.
* *order*: default ordering in currency pairs (more of this below).
* *roundoff*: number of decimal places

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
=======================

To use it::

    >>> import ccy
    >>> c = ccy.country('us')
    >>> c
    'United States'
    >>> ccy.countryccy('us')
    'USD'


Not all the country codes are standard
[http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 ISO 3166-1 alpha-2].
There is a function for adding extra pseudo-countries::

    import ccy
    ccy.set_new_country('EU','EUR','Eurozone')
    
Set a new country with code 'EU', currency 'EUR' named 'Eurozone'.
This pseudo country is set in the library already.

    
Requirements
================

* Python 2.6 or above, including Python 3
* pytz_ for Countries information.


Installation
~~~~~~~~~~~~~~~~

This library works for Python 2.6 and higher, including Python 3.

Using `easy_install`::

	easy_install ccy
	
Using `pip`::

	pip install ccy
	
From source::

	python setup.py install
	
It requires the pytz_ package.  
	
Runnung tests
~~~~~~~~~~~~~~~~~~~~~

From within the package directory::

	python runtests.py
	
	
.. _pytz: http://pytz.sourceforge.net/
.. _`ISO 3166-1 alpha-2`: http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
