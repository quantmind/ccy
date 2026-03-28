# Day Counters

The `DayCounter` enum provides standard day count conventions used in financial calculations.

## Available conventions

| Value | Description |
|-------|-------------|
| `ACT/360` | Actual days over 360 |
| `ACT/365` | Actual days over 365 |
| `30/360` | 30-day months over 360 (US/NASD convention) |
| `30E/360` | 30-day months over 360 (European convention — end date always capped at 30) |
| `ACT/ACT` | Actual days over actual days in the year |

## Usage

```python
from ccy import DayCounter
from datetime import date

start = date(2024, 1, 1)
end = date(2024, 7, 1)

dc = DayCounter.ACT360
print(dc.count(start, end))   # 182.0
print(dc.dcf(start, end))     # 0.5055...
```

Instantiate from its string value:

```python
dc = DayCounter("ACT/365")
print(dc.dcf(start, end))     # 0.4986...
```

Iterate over all conventions:

```python
for dc in DayCounter:
    print(dc.value, dc.dcf(start, end))
```

## Methods

### `count(start, end) -> float`

Returns the number of days between two dates. Accepts both `date` and `datetime` objects.

```python
from datetime import datetime, timezone

start = datetime(2024, 1, 1, 9, 0, tzinfo=timezone.utc)
end = datetime(2024, 1, 2, 15, 0, tzinfo=timezone.utc)

DayCounter.ACT360.count(start, end)  # 1.25
```

### `dcf(start, end) -> float`

Returns the day count fraction — the period length expressed as a fraction of a year, according to the convention.

```python
start = date(2024, 1, 1)
end = date(2025, 1, 1)

DayCounter.ACT365.dcf(start, end)   # 1.0027... (366 days / 365)
DayCounter.ACT360.dcf(start, end)   # 1.0166... (366 days / 360)
DayCounter.ACTACT.dcf(start, end)   # 1.0 (spans exactly one year)
DayCounter.THIRTY360.dcf(start, end) # 360.0 (30/360 raw result)
```
