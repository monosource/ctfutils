# ctfutils

A collection of Python methods to be used for CTFs.

## Installation

```
pip install git+git://github.com/monosource/ctfutils.git
```

## Usage

### String manipulation

```python
import ctfutils

some_string = '1234567890'

splits = list(ctfutils.chunks(some_string, 2))
```
