# sheffutils

## basic usage

The idea behind this is a single python file as a util.

You should be able to do:
```python3
import sheffutils
sheffutils.hello_world()
```

call a def directly
```python3
from sheffutils import hello_world
hello_world()
```

rename namespace if needed
```python3
from sheffutils import hello_world as hw
hw()
```

## Run tests:

I'm going to try and support `python 3.11.x` and up.

```python3
pip install pytest pytest-cov
pytest
```