# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['TRAMAS']

package_data = \
{'': ['*']}

install_requires = \
['pip',
 'robotframework>=4']

setup_kwargs = {
    'name': 'robotframework-creartramas',
    'version': '1.0.0',
    'description': 'Creacion de tramas en hexadecimal',
    'author': 'Anthony Arevalo',
    'maintainer': 'Anthony Arevalo',
    'url': 'https://pypi.org/project/robotframework-creartramas',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
