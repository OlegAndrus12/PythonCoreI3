# Python f-string / Format Cheatsheet

## Format spec syntax
```
{value:[fill][align][sign][#][0][width][grouping]["."precision][type]}
```

---

## Alignment
```python
x = 22
f"{x:< 10d}"   # left-aligned,   width 10  → "22        "
f"{x:10d}"     # right-aligned,  width 10  → "        22"
f"{x:^10d}"    # centered,       width 10  → "    22    "
```

Custom fill char goes before align:
```python
f"{x:=<10d}"   # left with '=' fill  → "22========"
f"{x:*^10x}"   # centered with '*'   → "****16****"
f"{x:h>10b}"   # right with 'h' fill → "hhhh10110"
```

---

## Number formatting
```python
n = 1234567.891

f"{n:,.2f}"    # 1,234,567.89   ← comma thousands sep
f"{n:_.2f}"    # 1_234_567.89   ← underscore sep
f"{n:.0f}"     # 1234568        ← no decimal
f"{n:.4f}"     # 1234567.8910   ← 4 decimal places
f"{n:e}"       # 1.234568e+06   ← scientific
f"{n:.2e}"     # 1.23e+06

f"{42:+d}"     # +42            ← always show sign
f"{7:05d}"     # 00007          ← zero-pad to width 5
```

Integer bases:
```python
num = 255
f"{num:b}"     # 11111111  binary
f"{num:o}"     # 377       octal
f"{num:x}"     # ff        hex lower
f"{num:X}"     # FF        hex upper
f"{num:#x}"    # 0xff      with prefix
```

Percentage:
```python
f"{19/22:.2%}"   # 86.36%
f"{0.764:.1%}"   # 76.4%
```

Dynamic width/precision:
```python
width, precision = 12, 3
f"{3.14159:{width}.{precision}f}"   # "       3.142"
```

---

## f-string power features
```python
name = "Oleh"

f"{name!r}"        # 'Oleh'  — repr(), adds quotes
f"{name!s}"        # Oleh    — str() (default)
f"{name!a}"        # 'Oleh'  — ascii(), escapes non-ASCII

x = 42
f"{x=}"            # x=42       — debug shortcut (3.8+)
f"{x=:.2f}"        # x=42.00

# inline expression
score = 73
f"{'pass' if score >= 60 else 'fail'}"   # pass

# multiline — concatenate f-strings in parens
card = (
    f"Name: {name}\n"
    f"Adult: {25 >= 18}"
)
```

---

## Special escape sequences
```python
"\n"   # newline
"\t"   # horizontal tab
"\r"   # carriage return (moves cursor to line start)
"\f"   # form feed / new page
"\v"   # vertical tab
```
