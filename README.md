# sheffutils
basic python utils I need.

The idea behind this file is a single file as a util.

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

rename namespace
```python3
from sheffutils import hello_world as hw
hw()
```

Run tests:
```python3
pip install pytest pytest-cov
pytest
```