0.6.1 - 2014 Apr 14
===========================
* Bug fixes
* **40 regression tests** with **72%** coverage

0.6.0 - 2014 Jan 14
===========================
* pep8
* Removed date parser and added dependency to dateutils_
* Added travis CI
* Development moved to github
* Added sphinx docs
* Removed the ``web`` module
* Better period calculations
* **39 regression tests** with **72%** coverage

0.5.1 - 2011 Jun 16
===========================
* Bug fixes.
* 19 tests

0.5.0 - 2011 May 12
===========================
* Ported to Python 3 and dropped ``python-dateutil`` dependency.
* Moved the ``django`` application ``basket`` into the ``web`` module.
* 19 tests

0.4.1 - 2010 Dec 03
==========================
* Added ``ccy.web`` module for currency and date tools for the web.

0.4 - 2010 Oct 10
==========================
* Development status set to Alpha.
* installation fix.

0.3.9  - 2010 Sep 24
=============================
* Minor release.
* Added javascript timestamp converter.
* Timestamp tests failing. Closing them untill 0.4 release.
* 19 tests.

0.3.8  - 2010 Sep 12
=============================
* Added python-dateutil dependency
* To run tests use ``ccy.runtests``
* 21 tests.

0.3.7  - 2010 June 22
=============================
* Added new module date converters

0.3.5  - 2010 June 07
=============================
* Added new module dates with period manipulation
* Moved all tests into the tests module

0.3.4  - 2010 April 25
=============================
* Added trading centres for calculation of trading holidays (requires python-dateutil)
* This feature is still very much alpha.

0.3.3  - 2010 March 31
=============================
* Added `ccy.basket.media` to `MANIFEST.in`

0.3.2  - 2010 March 30
=============================
* Added `ccy.basket` module, a django application for managing basket of currencies.

0.3
==============
* Added as_cross to ccy class to display the currency as a cross FX string
* Added 2 shortcuts to display crosses: cross(eur) -> EURUSD, and crossover(eur) -> EUR/USD

0.2
==============
* Rearranged the modules so that data-structures and data are separated.
* Added symbol property to ccy
* bug fixes and refactoring for python 3.1 compatibility
* Added another 2 tests

0.1.2
============
* First official release


.. _dateutils: https://pypi.python.org/pypi/python-dateutil
