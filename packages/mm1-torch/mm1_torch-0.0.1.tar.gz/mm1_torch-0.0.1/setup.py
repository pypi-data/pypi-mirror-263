# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mm1_torch']

package_data = \
{'': ['*']}

install_requires = \
['einops', 'torch', 'zetascale']

setup_kwargs = {
    'name': 'mm1-torch',
    'version': '0.0.1',
    'description': 'MM1 - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# MM1 \nPyTorch Implementation of the paper "MM1: Methods, Analysis & Insights from Multimodal LLM Pre-training".\n\n`img -> encoder -> connector -> llm -> tokens`\xa0\n\n\n\n# License\nMIT\n',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/mm1',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
