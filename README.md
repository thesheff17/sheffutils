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

## Running github actions locally

make sure you have docker installed already and running.

install this extention `Github Local Actions`

clone this repo:
https://github.com/nektos/act
`make install`

I had some permission problems and had to adjust the directory some directory using `chown`

Set artifact location for github actions
```
echo "--artifact-server-path $HOME/.act" >> $HOME/.actrc\n
```

now on the left side of vscode you should be able to click play on the Workflows and the jobs should run and pass.  It will also dump artifacts into `$HOME/.actrc/<jobNumber>/<python-version>/*.zip`