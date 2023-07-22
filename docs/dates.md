---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.7
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Dates & Periods

The module is shipped with a ``date`` module for manipulating time periods and 
converting dates between different formats. Th  *period* function can be use 
to create ``Period`` instanc.::

```{code-cell} ipython3
import ccy
p = ccy.period("1m")
p
```

```{code-cell} ipython3
p += "2w"
p
```

```{code-cell} ipython3
p += "3m"
p
```

```{code-cell} ipython3
p -= "1w"
p
```

```{code-cell} ipython3
p -= "1w"
p
```

```{code-cell} ipython3
p -= "1w"
p
```

```{code-cell} ipython3

```
