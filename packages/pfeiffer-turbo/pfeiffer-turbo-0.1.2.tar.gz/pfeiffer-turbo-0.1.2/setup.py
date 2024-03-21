# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pfeiffer_turbo']

package_data = \
{'': ['*']}

install_requires = \
['PyVISA>=1.13.0,<2.0.0']

setup_kwargs = {
    'name': 'pfeiffer-turbo',
    'version': '0.1.2',
    'description': '',
    'long_description': '# pfeiffer-turbo\n[![Python versions on PyPI](https://img.shields.io/pypi/pyversions/pfeiffer-turbo.svg)](https://pypi.python.org/pypi/pfeiffer-turbo/)\n[![pfeiffer-turbo version on PyPI](https://img.shields.io/pypi/v/pfeiffer-turbo.svg "pfeiffer-turbo on PyPI")](https://pypi.python.org/pypi/pfeiffer-turbo/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)  \nPython interface RS485 connections for Pfeiffer HiPace turbo drive units. Currently only the TM700 is implemented. Also supports connecting through a TCPIP socket, e.g. when using a serial to TCPIP converter for the turbo controller.\n\n## Example\n### RS485 connection example\n```python\nfrom pfeiffer_turbo import TM700\n\npump = TM700(resource_name = "COM9", address = 1)\n\n# get the rotation speed in Hz\npump.actual_spd\n\n# start the pump\npump.start()\n\n# stop the pump\npump.stop()\n```\n### TCPIP connection example\n```python\nfrom pfeiffer_turbo import TM700\n\npump = TM700(\n    resource_name="10.10.222.8:12345", address=1, connection_type=ConnectionType.TCPIP\n)\n\n# get the rotation speed in Hz\npump.actual_spd\n\n# start the pump\npump.start()\n\n# stop the pump\npump.stop()\n```\n\n## Implementation\nA baseclass `DriveUnit`:\n```Python\nclass DriveUnit:\n    def __init__(\n        self,\n        resource_name: str,\n        address: int,\n        connection_type: ConnectionType,\n        supported_parameters: Sequence[int],\n    ):\n```\ntakes in a set of integers that correspond to pfeiffer vacuum parameters supported by the particular drive unit. Implemented vacuum parameters are seen in `parameters.py`. The getters and setters are then dynamically generated based on the `supported_parameters` and info in `parameters.py`; the enum `Parameters` contains all implemented pfeiffer vacuum parameters, and the dictionary `parameters` contains key, value pairs of `Parameters` and `ParameterInfo`, where `ParameterInfo` is a dataclass containing the implemenation information for a particular parameter:\n```Python\n@dataclass\nclass Parameter:\n    designation: str\n    data_type: DataType\n    access: StopIteration\n    min: Optional[int] = None\n    max: Optional[int] = None\n    unit: Optional[str] = None\n    default: Optional[Union[int, float, str]] = None\n    options: Optional[dict[int, str]] = None\n```\nImplementing new drive units is be done by inheriting from `DriveUnit` and specifying which pfeiffer parameters are supported by the specific model. New parameters can be implemented by extending the `Parameters` enum and `parameters` dictionary. The class attributes are named similarly to the Pfeiffer vacuum parameters, with underscores inserted between uppercase - lowercase transitions and all lowercase letters. E.g. `GasMode` -> `gas_mode`.',
    'author': 'ograsdijk',
    'author_email': 'o.grasdijk@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ograsdijk/pfeiffer-turbo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
