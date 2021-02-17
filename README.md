# How to make python script executable

The best way, which is cross-platform, is to create `setup.py`, define an entry point in it and install with `pip`.

Say you have the following contents of `myscript.py`:

```python
def run():
    print('Hello world')
```

Then you add setup.py with the following:

```python
from setuptools import setup
setup(
    name='myscript',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'myscript=myscript:run'
        ]
    }
)
```

Entry point format is
`terminal_command_name=python_script_name:main_method_name`

Finally install with the following command.

```shell
pip install -e /path/to/script/folder
```

`-e` stands for editable, meaning you'll be able to work on the script and invoke the latest version without need to reinstall

After that you can run `myscript` from any directory.
