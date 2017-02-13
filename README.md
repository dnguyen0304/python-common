Python Common
-------------
Shared Python libraries.

Getting Started
---------------
Note the following methods are **not** compatible.

### pip
If you primarily use `pip` to install dependencies, from the terminal run
```
$ pip install --editable git+https://github.com/dnguyen0304/python-common.git@master#egg=common-1.0
$ pip freeze > requirements.txt
```

In future builds, from the terminal run
```
$ pip install --requirement requirements.txt
```

### setuptools
If you primarily use `setuptools` to install dependencies, update `setup.py`.
```
setup(...,
      install_requires=['common==1.0'],
      dependency_links=['git+https://github.com/dnguyen0304/python-common.git@master#egg=common-1.0'])
```

In future builds, from the terminal run
```
$ python setup.py install
```

### Details
It is possible to specify particular transport protocols, branches, tags, or commits as well. See the `pip install` [documentation here](https://pip.readthedocs.io/en/stable/reference/pip_install/#git) for more details.