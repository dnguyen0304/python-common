Introduction
------------
This document adheres to the specifications outlined in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

Source Control
--------------
### Commit Messages
- Issue IDs **should** be included.
```
# YES
git commit --message "PROJECT-1: foo"

# No
git commit --message "foo"
```

Python
------
### General
- Packages **should** have `__all__` indices in their `__init__.py`.
- `__all__` indices **should** be sorted alphabetically.
- Modules **should not** have `__all__` indices.
- Package base classes **must** be named `Base`.
```
# YES
class Base:
    pass

# No
class BaseFoo:
    pass
```
- Classes **should** implement `__repr__` methods.

### Models
- Models **should not** have docstrings.