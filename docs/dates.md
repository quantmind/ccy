# Dates & Periods

The module is shipped with a `date` module for manipulating time periods and
converting dates between different formats. The *period* function can be used
to create `Period` instances:

```python
import ccy
p = ccy.period("1m")
p
```

```python
p += "2w"
p
```

```python
p += "3m"
p
```

```python
p -= "1w"
p
```
