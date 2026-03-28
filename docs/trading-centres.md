# Trading Centres

Trading centres provide business day calendars for financial date calculations.
A [TradingCentre][ccy.tradingcentres.TradingCentre] wraps a single holiday calendar.
[TradingCentres][ccy.tradingcentres.TradingCentres] combines multiple centres for joint business day calculations.

!!! note "Installation"
    This feature requires the `holidays` extra:
    ```bash
    pip install ccy[holidays]
    ```

## Available centres

| Code | Description |
|------|-------------|
| `TGT` | TARGET (European Central Bank) |
| `LON` | London (United Kingdom) |
| `NY` | New York (United States) |

## Functions

::: ccy.tradingcentres.centres

::: ccy.tradingcentres.nextbizday

::: ccy.tradingcentres.prevbizday

## Classes

::: ccy.tradingcentres.TradingCentre

::: ccy.tradingcentres.TradingCentres

## Usage

### Business day checks

```python
from datetime import date
from ccy.tradingcentres import centres

tcs = centres("TGT")
tcs.isbizday(date(2024, 12, 25))  # False — Christmas
tcs.isbizday(date(2024, 12, 24))  # True
```

Combine multiple centres — a day is a business day only if it is in all of them:

```python
tcs = centres("LON,NY")
tcs.code  # "LON,NY"
tcs.isbizday(date(2024, 7, 4))  # False — US Independence Day
```

### Next and previous business day

```python
from ccy.tradingcentres import nextbizday, prevbizday
from datetime import date

friday = date(2024, 12, 20)

nextbizday(friday)        # date(2024, 12, 23) — skips weekend
nextbizday(friday, nd=2)  # date(2024, 12, 24)

prevbizday(friday)        # date(2024, 12, 19)
prevbizday(friday, nd=3)  # date(2024, 12, 17)
```

Pass a centre code to apply its holiday calendar:

```python
nextbizday(date(2024, 12, 24), tcs="TGT")  # date(2024, 12, 27) — skips Christmas
```

### `nd=0` — adjust to business day

Passing `nd=0` to `nextbizday` adjusts the date forward to the next business day if it falls on a weekend or holiday, and leaves it unchanged otherwise:

```python
saturday = date(2024, 12, 21)
nextbizday(saturday, nd=0)  # date(2024, 12, 23)
nextbizday(friday, nd=0)    # date(2024, 12, 20) — already a business day
```
