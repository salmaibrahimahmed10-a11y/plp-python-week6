# Week 6 Assignment - Error Handling

## Files

- `safe_tools.py` - Contains three functions that safely handle division, number conversion, and dictionary key lookup.
- `unbreakable.py` - Demonstrates the idea of handling errors so a program can continue running instead of crashing.
- `README.md` - Describes the assignment files and explains why an `if` check alone cannot catch `abc`.

## Why can't the `if` check catch `abc` on its own?

An `if` check cannot catch `abc` when using `int()` because the conversion happens before the program can perform the check. The `int()` conversion raises a `ValueError`, so `try`/`except` is needed to safely handle the invalid input.
