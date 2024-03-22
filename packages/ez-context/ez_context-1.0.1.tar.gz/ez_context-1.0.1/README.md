# EZ Context Managers

Allows you to create generator-based context managers without try/finally.
Fully static-typed and thread-safe.

Example:
```python
@context_mgr
def example():
    print("entering")
    yield
    print("exiting")

with example as ex:
    print("Hello World!")
    
```
```
entering
Hello World!
exiting
```

## Detailed Example:

```python
@context_mgr
def random_value(a=0, b=100):
    rand_num: int = random.randint(a, b)
    print(f"entering {rand_num}")

    # `yield` runs the body of the `with` statement.
    # The yielded value is stored in VAR by `with ... as VAR`
    error = yield rand_num
    # If the body raises an Exception, it's returned here.
    # Otherwise, None is returned

    print(f"exiting {rand_num}, {error=}")
    if isinstance(error, ValueError):
        # Return True to suppress the Exception
        return True


with random_value(-5, -1) as n:
    assert_type(n, int)  # statically typed!
    print(n)

# Parentheses are optional if there are no arguments.
with random_value as n1:

    # Reusable and re-entrant
    with random_value as n2:
        raise ValueError("CoolBeans")

```



Created for a comment on [this mCoding video](https://www.youtube.com/watch?v=LBJlGwJ899Y&t=36s).