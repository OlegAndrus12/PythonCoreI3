# Python Core — iteration 3

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?style=flat-square)](LICENSE)

Lecture materials for the Python Core course. Each module is one lecture: a folder of small, runnable
scripts, each making **one idea** concrete — run it, change it, read why the output changed.

<img src="yoda.jpg" alt="May the Force be with you" width="280">

```
├── module01/   Data types: numbers, strings, collections, mutability and memory
├── module02/   Control flow, exceptions and functions
├── module03/   datetime, time zones and random
├── module04/   String formatting, string methods and regular expressions
├── module05/   Files: open(), modes, pathlib and shutil
├── module06/   Modules, packages, pip and publishing
├── module07/   collections, decimal, iterators and generators
├── module08/   Functional programming: closures, decorators, comprehensions
├── module09/   OOP: classes, encapsulation, inheritance, MRO, polymorphism
├── module10/   Properties, magic methods, custom iterators and containers
├── module11/   OOP practice: composition, class decorators, Enum + match
├── module12/   Serialization: JSON, pickle, YAML and pydantic
```

Also at the root: **[Tech interview checklist.md](Tech%20interview%20checklist.md)** — questions for a
junior Python developer interview, covering the whole course.

**Conventions used throughout:**

- Every module has an `agenda.md` with the lecture plan (in Ukrainian). Code and comments are in English.
- Every script runs on its own: `python module01/lists/basics.py`.
- Scripts that read or write files use paths relative to their own folder — `cd` into the folder first.
- Some scripts are interactive and wait for `input()`.
- Python 3.10+ (`match` statements appear in module08 and module11).

**Third-party packages.** Modules 01, 02, 04, 05, 07–10 use only the standard library. The rest need:

| Module | Packages |
| --- | --- |
| module03 | `pytz`, `python-dateutil` |
| module06 | `rich`, `plotext` |
| module11 | `requests`, `beautifulsoup4` |
| module12 | `pydantic`, `pydantic-settings`, `python-dotenv`, `faker`, `requests`, `pyyaml`, `rich`, `prompt_toolkit`, `prettytable`, `asciimatics`, `cowsay`, `art` |

```bash
python -m venv .venv && source .venv/bin/activate
pip install rich requests   # whatever the module you are running needs
```

---

# Module 01 — Data types

What every built-in type is, what it can do, and the one property that explains most surprises:
whether it can change in place.

| Folder / file | What it covers |
| --- | --- |
| **[python-data-types.html](module01/python-data-types.html)** | Interactive cheat sheet — every built-in type, all its public methods, with results from a real CPython run. Open it in a browser |
| **[memory/](module01/memory/)** | `id()`, names as references, `copy` vs `deepcopy`; [visualizer.html](module01/memory/visualizer.html) draws names and objects in memory |
| **[lists/](module01/lists/)** · **[tuples/](module01/tuples/)** · **[sets/](module01/sets/)** · **[dicts/](module01/dicts/)** · **[strings/](module01/strings/)** | The basics of each type on everyday data — a playlist, a user profile; [tuples/use_cases.py](module01/tuples/use_cases.py) shows where a tuple beats a list |
| **[conversions/](module01/conversions/)** | Converting between `int`, `float`, `bool`, `str` and `None`, and what each conversion loses |
| **[deposit.py](module01/deposit.py)** | Compound interest — numbers and operators in one small real calculation |

Reference sheets in the same folder:

| File | Shows |
| --- | --- |
| [collections.md](module01/collections.md) | `list` / `tuple` / `set` / `dict` / `str` side by side, plus time complexity of each operation |
| [comparison.png](module01/comparison.png) | `list` vs `tuple` vs `set` at a glance |
| [mutable_vs_immutable.png](module01/mutable_vs_immutable.png) | Which built-in types are mutable |
| [prios.png](module01/prios.png) | Operator precedence |
| [strong_dynamic.txt](module01/strong_dynamic.txt) | Static vs dynamic typing — advantages and disadvantages |

📋 Full topic list: **[module01/agenda.md](module01/agenda.md)**

---

# Module 02 — Control flow, exceptions and functions

| Folder | What it covers |
| --- | --- |
| **[if_statements/](module02/if_statements/)** | `if` / `elif` / `else`, `and` / `or`, `in`, the ternary operator, a leap-year exercise |
| **[for_loop/](module02/for_loop/)** | `for`, `break` / `continue`, `enumerate`, `zip`, nested loops, building collections in a loop |
| **[while_loop/](module02/while_loop/)** | `while` — a guessing game, a digit sum, a text menu |
| **[exceptions/](module02/exceptions/)** | `try` / `except` / `else` / `finally`, `raise`, common errors like `KeyError`, input validation; [exception.png](module02/exceptions/exception.png) is the exception hierarchy |
| **[functional/](module02/functional/)** | Four steps: defining and calling functions → local and global scope → `*args` / `**kwargs` → recursion (factorial, Fibonacci, recursion vs iteration) |

[statements.pdf](module02/statements.pdf) — control-flow diagrams for the statements above.

📋 Full topic list: **[module02/agenda.md](module02/agenda.md)**

---

# Module 03 — datetime, time zones and random

| Folder | What it covers |
| --- | --- |
| **[date/](module03/date/)** | `datetime`, `date`, `timedelta`, `strftime` / `strptime`, `combine`, `MINYEAR`, the `calendar` module, `time.sleep` — and time zones three ways: `pytz`, `dateutil`, and the standard library's `zoneinfo` |
| **[random/](module03/random/)** | `randint`, `random`, `choice`, `choices`, `sample`, `shuffle` — coin flips and a licence-plate generator |

[formats.md](module03/formats.md) — every `strftime` / `strptime` format code, each with an example.

📋 Full topic list: **[module03/agenda.md](module03/agenda.md)**

---

# Module 04 — String formatting, string methods and regular expressions

| Folder | What it covers |
| --- | --- |
| **[formated_string/](module04/formated_string/)** | The format-spec mini-language, f-strings, number formatting, escape characters; [cheatsheet.md](module04/formated_string/cheatsheet.md) |
| **[methods/](module04/methods/)** | `split`, `join`, `strip`, `find`, `replace`, `translate`, `isdigit` / `isalpha`, case methods — and practice tasks: a slug generator, a password checker, a content moderator |
| **[reg/](module04/reg/)** | The `re` module: `match` vs `search`, `findall`, `sub`, `split`, anchors, groups — on real tasks: e-mails, URLs, IPs, phone numbers, card masking, prices, hashtags; [cheatsheet.md](module04/reg/cheatsheet.md) |
| **[ip_aggregator/](module04/ip_aggregator/)** | Counting IP addresses in a log file — a straightforward version and a tidier one |

📋 Full topic list: **[module04/agenda.md](module04/agenda.md)**

---

# Module 05 — Files

Run these from inside `module05/` — they work on the sample files next to them.

| Folder / file | What it covers |
| --- | --- |
| **[_open/](module05/_open/)** | `open()` and its modes (`r`, `w`, `a`, `x`, `b`, `+`), `read` / `readline`, writing, encodings, binary files, `seek` / `tell`, `with` |
| **[_pathlib.py](module05/_pathlib.py)** · **[_pathlib2.py](module05/_pathlib2.py)** | `pathlib` basics, then sorting files into folders by extension |
| **[_cp.py](module05/_cp.py)** · **[_mv.py](module05/_mv.py)** · **[_archive.py](module05/_archive.py)** | Copying, moving and archiving with `shutil` |
| [picture/](module05/picture/) · [source/](module05/source/) · [Temp/](module05/Temp/) | Sample files for the scripts above to work on |

📋 Full topic list: **[module05/agenda.md](module05/agenda.md)**

---

# Module 06 — Modules, packages, pip and publishing

| Folder / file | What it covers |
| --- | --- |
| **[cheetsheet.md](module06/cheetsheet.md)** | How `import` finds things, module vs package vs script, `pip`, virtual environments, publishing |
| **[all_example/](module06/all_example/)** | A package whose `__init__.py` and `__all__` decide what `from shapes import *` brings in |
| **[moskali/](module06/moskali/)** | A real installable CLI package (`pyproject.toml`, `argparse`, `rich` tables, `plotext` charts) that visualises Russian military losses data published by the General Staff of Ukraine. Its own [README](module06/moskali/README.md) covers building and publishing to PyPI |
| **[console_rich.py](module06/console_rich.py)** · **[utils.py](module06/utils.py)** | Using a third-party package — `rich` tables and progress bars |

---

# Module 07 — collections, decimal, iterators and generators

| Folder / file | What it covers |
| --- | --- |
| **[_namedtuple.py](module07/_namedtuple.py)** | `namedtuple` as a first step towards classes |
| **[_counter/](module07/_counter/)** | `Counter`: letter frequencies, an anagram check, temperature readings |
| **[_defdict.py](module07/_defdict.py)** | `defaultdict`: grouping phone numbers by mobile operator |
| **[decimal/](module07/decimal/)** | Why `0.1 + 0.2 != 0.3`, `Decimal` precision, rounding modes, comparison |
| **[iterators_vs_generators.md](module07/iterators_vs_generators.md)** | Iterators and generators compared feature by feature, with examples |

📋 Full topic list: **[module07/agenda.md](module07/agenda.md)**

---

# Module 08 — Functional programming

| Folder | What it covers |
| --- | --- |
| **[func_as_object/](module08/func_as_object/)** | Functions as values, pipelines, closures, currying, callbacks (an event emitter, payment callbacks) |
| **[decorators/](module08/decorators/)** | From execution order to real decorators: timer, retry, rate limit, permission check, error logging, caching to a file, `lru_cache`, decorators with parameters |
| **[comprehensions/](module08/comprehensions/)** | `list` and `dict` comprehensions |
| **[exercises/](module08/exercises/)** | `lambda`, `map`, `filter`, `reduce`, `any` / `all`, `zip`, `enumerate` on an employee dataset, and a timing comparison; [cheatsheet.md](module08/exercises/cheatsheet.md) compares `map` / `filter` with comprehensions |

📋 Full topic list: **[module08/agenda.md](module08/agenda.md)**

---

# Module 09 — Object-oriented programming

| File | What it covers |
| --- | --- |
| **[repository.py](module09/repository.py)** | Anatomy of a class: `__init__`, `self`, instance vs class attributes |
| **[encapsulate.py](module09/encapsulate.py)** | public, `_protected` and `__private` |
| **[inheritance.py](module09/inheritance.py)** · **[inheritance_02.py](module09/inheritance_02.py)** | Single and multi-level inheritance |
| **[mro_01.py](module09/mro_01.py)** · **[mro_02.py](module09/mro_02.py)** · **[multiple_inheritance.py](module09/multiple_inheritance.py)** | `super()`, method resolution order (C3), mixins |
| **[polymorphism_01.py](module09/polymorphism_01.py)** · **[polymorphism_02.py](module09/polymorphism_02.py)** | Polymorphism and duck typing |
| **[abc_01.py](module09/abc_01.py)** · **[abc_02.py](module09/abc_02.py)** | Abstract base classes |

[oop.png](module09/oop.png) — the four principles on one diagram.

📋 Full topic list: **[module09/agenda.md](module09/agenda.md)**

---

# Module 10 — Special methods and object control

| Folder / file | What it covers |
| --- | --- |
| **[setter_getter.py](module10/setter_getter.py)** · **[properties/](module10/properties/)** | Getters and setters, then `@property`: a bank account, a product with a discount |
| **[magic/](module10/magic/)** | Magic methods on a car and a shopping cart |
| **[iterator/](module10/iterator/)** | Custom iterators and their generator equivalents: date ranges, pagination, random numbers |
| **[containers/](module10/containers/)** | Extending `UserList`, `UserDict` and `UserString` |
| **[copy_deepcopy.py](module10/copy_deepcopy.py)** | Shallow vs deep copy |
| **[abc_ex.py](module10/abc_ex.py)** | `ABC` vs `metaclass=ABCMeta` |

📋 Full topic list: **[module10/agenda.md](module10/agenda.md)**

---

# Module 11 — OOP practice

| File | What it covers |
| --- | --- |
| **[aggr_comp.py](module11/aggr_comp.py)** | Aggregation vs composition |
| **[class_static_methods.py](module11/class_static_methods.py)** | `@classmethod` as an alternative constructor, `@staticmethod` for validation |
| **[class_decorator.py](module11/class_decorator.py)** | A singleton built with a class decorator |
| **[defdict.py](module11/defdict.py)** | Writing your own `defaultdict` |
| **[enum_match.py](module11/enum_match.py)** | `Enum` with `match` / `case` |
| **[fp_ex.py](module11/fp_ex.py)** · **[oop_ex.py](module11/oop_ex.py)** | The same quote scraper (`requests` + BeautifulSoup) written in functional style and with classes |

---

# Module 12 — Serialization

| Folder / file | What it covers |
| --- | --- |
| **[json/](module12/json/)** | `json.dump` / `load` / `dumps` / `loads`, formatting options, non-ASCII text, JSON vs `pickle`, data from a public API |
| **[yaml/](module12/yaml/)** | Reading and writing YAML with PyYAML, loading a config file |
| **[pydantic_ex/](module12/pydantic_ex/)** | pydantic v2: models, lax vs strict validation, `Field` and aliases, field and model validators, computed fields, custom serializers, `model_copy`, `extra="forbid"`, settings from `.env` |
| **[fancy_console/](module12/fancy_console/)** | Console output beyond `print`: `rich`, `prettytable`, `asciimatics`, `cowsay`, `art`, `prompt_toolkit` |
| **[file_logger.py](module12/file_logger.py)** | `logging` to the console and a file at different levels |

📋 Full topic list: **[module12/agenda.md](module12/agenda.md)**

