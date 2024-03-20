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
    'version': '0.0.3',
    'description': 'MM1 - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# MM1 \nPyTorch Implementation of the paper "MM1: Methods, Analysis & Insights from Multimodal LLM Pre-training".\n\n`img -> encoder -> connector -> llm -> tokens`\xa0\n\n## install\n`pip3 install mm1-torch`\n\n## usage\n```python\n\nimport torch\nfrom mm1_torch.main import MM1\n\n# Tensors\nx = torch.randint(0, 100, (1, 512))\nimg = torch.randn(1, 3, 224, 224)\n\n# Create a model\nmodel = MM1(\n    dim=512,\n    depth=12,\n    heads=8,\n    dim_head=64,\n    dropout=0.1,\n    num_experts=4,\n    num_experts_per_tok=2,\n)\n\n\n# Forward\nout = model(x, img)\nprint(out.shape)  # torch.Size([2, 3, 512])\n```\n\n### `CAbstractor`\n\n```python\nimport torch \nfrom mm1_torch.main import CAbstractor\n\n# Tensors\nx = torch.randn(1, 3, 224, 224)\n\n# Create a model\nmodel = CAbstractor(\n    dim=512,\n    depth=12,\n    heads=8,\n)\n\n\n# Forward\nout = model(x)\nprint(out.shape)  # torch.Size([2, 3, 512])\n\n\n```\n\n\n# License\nMIT\n',
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
