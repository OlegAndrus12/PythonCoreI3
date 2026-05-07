# Iterators vs Generators in Python

| Feature | Iterator | Generator |
|---|---|---|
| **Definition** | Object implementing `__iter__` and `__next__` | Function using `yield` (or generator expression) |
| **Creation** | Class with `__iter__`/`__next__` methods | `def` with `yield`, or `(x for x in ...)` |
| **State management** | Manual — stored in instance variables | Automatic — Python suspends and resumes the frame |
| **Memory usage** | Depends on implementation | Lazy — values produced one at a time |
| **Code volume** | More boilerplate | Concise |
| **`return` behavior** | Normal method return | Raises `StopIteration` with optional value |
| **`send()` support** | No | Yes — can receive values via `yield` |
| **`throw()` support** | No | Yes — can inject exceptions |
| **Reusability** | Can reset state if implemented | Not reusable once exhausted |
| **`isinstance` check** | `Iterable` / `Iterator` | `Generator` (subtype of `Iterator`) |
| **Use case** | Complex stateful iteration, reusable objects | Pipelines, lazy sequences, coroutines |

## Quick examples

### Iterator

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for n in Countdown(3):
    print(n)  # 3, 2, 1
```

### Generator

```python
def countdown(start):
    while start > 0:
        yield start
        start -= 1

for n in countdown(3):
    print(n)  # 3, 2, 1
```

### Generator expression

```python
squares = (x**2 for x in range(10))  # lazy, no list built
```