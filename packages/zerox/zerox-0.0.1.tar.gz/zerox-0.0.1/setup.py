# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zerox']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.68.0,<0.69.0',
 'httpx>=0.19.0,<0.20.0',
 'pydantic>=1.9.0,<2.0.0',
 'uvicorn>=0.15.0,<0.16.0']

setup_kwargs = {
    'name': 'zerox',
    'version': '0.0.1',
    'description': 'Paper - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n\n# zero\nA Reliable, Customize-able, and Scalable Zapier Alternative for Production-Grade Workflow Automation\n\nZero is a reliable and customizable Zapier alternative that offers production-grade workflow automation. Our platform seamlessly integrates and automates processes for businesses of all sizes. Eliminate manual work and focus on more important tasks with our extensive features and customization options. Our platform is built to handle high volumes of data and transactions without compromising performance, ensuring reliable automation. As your business grows, our scalable platform can accommodate increased workloads. Our user-friendly interface allows anyone to create and manage workflows without complex coding. Experience the power of Zero and revolutionize your business automation today.\n\n\n# License\nMIT\n',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/paper',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
