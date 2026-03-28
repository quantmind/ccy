# Python CCY

## Getting Started

* installation
```bash
pip install ccy
```
* display currencies

```python
import ccy
import pandas as pd
df = pd.DataFrame(ccy.dump_currency_table())
df.head(80)
```

## Main Usage

```python
import ccy
eur = ccy.currency("aud")
eur.printinfo()
```

A currency object has the following properties:

* *code*: the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) three letters code.
* *twoletterscode*: two letter code.
* *default_country*: the default [ISO 3166-1 alpha_2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code for the currency.
* *isonumber*: the ISO 4217 number.
* *name*: the name of the currency.
* *order*: default ordering in currency pairs (more of this below).
* *rounding*: number of decimal places

## Currency Crosses

You can create currency pairs by using the `currency_pair` function:

```python
c = ccy.currency_pair("eurusd")
c
```

```python
c.mkt()
```

```python
c = ccy.currency_pair("chfusd")
c.mkt()  # market convention pair
```

## cross & crossover

Some shortcuts:

```python
ccy.cross("aud")
```

```python
ccy.crossover('eur')
```

```python
ccy.crossover('chf')
```

```python
ccy.crossover('aud')
```

Note, the Swiss franc cross is represented as 'USD/CHF', while the Aussie Dollar and Euro crosses are represented with the USD as denominator. This is the market convention which is handled by the order property of a currency object.

## Eurozone

The euro area, commonly called the eurozone (EZ), is a currency union of 20 member states of the European Union (EU) that have adopted the euro (€) as their primary currency and sole legal tender, and have thus fully implemented EMU policies.

```python
ccy.eurozone
```

```python
ccy.print_eurozone()
```
