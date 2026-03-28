# Dates & Periods

The `Period` class represents a calendar period composed of months and days.
Use the `period` factory function to create instances from a period string.

## Period strings

A period string combines one or more components, each a number followed by a unit letter:

| Unit | Meaning |
|------|---------|
| `Y`  | Years   |
| `M`  | Months  |
| `W`  | Weeks   |
| `D`  | Days    |

Examples: `"1Y"`, `"6M"`, `"2W"`, `"3D"`, `"1Y6M"`, `"2W3D"`.

## Usage

```python
import ccy

p = ccy.period("1Y6M")
str(p)       # "1Y6M"
p.years      # 1
p.months     # 6
p.totaldays  # 390
```

Arithmetic with strings or other `Period` objects:

```python
p = ccy.period("1M")
p += "2W"    # Period("1M2W")
p += "3M"    # Period("4M2W")
p -= "1W"    # Period("4M1W")
```

Comparison:

```python
ccy.period("1Y") > ccy.period("6M")   # True
ccy.period("12M") == ccy.period("1Y") # True
```

## Class reference

::: ccy.dates.period.Period
