# sheffutils

## basic usage

The idea behind this is a single python file as a util.

Get the `sheffutils.py` file:
```python3
wget https://raw.githubusercontent.com/thesheff17/sheffutils/refs/heads/main/sheffutils.py
```

## How can I support this project?

[buymeacoffee.com/thesheff17](https://buymeacoffee.com/thesheff17)


## Which python version is supported?  
I'm giong to try and support python `3.11.x` and up. `pytest` must pass on each version to merge code with [github actions.](https://github.com/thesheff17/sheffutils/actions)

## Usage

```python
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

## How do I handle versions, upgrades, supporting previous versions of this script?

I won't release any versions or have any official releases of this package/script.  You should know what you are running if you are using this code.  If you want to assign a version to the `sheffutils.py` file at the time of download you can.  I will do my best to not break backwards compatibility of anything I write.

I would much rather maintain multiple `def` doing slightly different things even if that means duplicating some code.  The reason for this is because it will maintain backwards compatibility for users running this script while also testing new code at the same time.  
 
 ## How can I add feature or fix a problem?
If you know how to fix it please make a pull request. If not please log an issue [here.](https://github.com/thesheff17/sheffutils/issues)
## Do you use AI to write code? 
yes if you look at some of the tools you can see stuff is wrapped around `ollama` commands.  All code should have unit tests defined in `test_sheffutils.py`