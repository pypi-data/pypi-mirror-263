# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['contaminante']

package_data = \
{'': ['*']}

install_requires = \
['astropy>=4.3.1,<5.0.0',
 'lightkurve>=2.0.11,<3.0.0',
 'matplotlib>=3.4.3,<4.0.0',
 'numpy>=1.21.3,<2.0.0',
 'pandas>=1.3.4,<2.0.0',
 'scipy>=1.7.1,<2.0.0',
 'tqdm>=4.62.3,<5.0.0']

setup_kwargs = {
    'name': 'contaminante',
    'version': '0.5.7',
    'description': "A package to help find the contaminant transiting source in NASA's *Kepler*, *K2* or *TESS* data.",
    'long_description': 'None',
    'author': 'Christina Hedges',
    'author_email': 'christina.l.hedges@nasa.gov',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
