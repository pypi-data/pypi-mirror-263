# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mxcubeweb',
 'mxcubeweb.core',
 'mxcubeweb.core.adapter',
 'mxcubeweb.core.components',
 'mxcubeweb.core.components.user',
 'mxcubeweb.core.models',
 'mxcubeweb.core.util',
 'mxcubeweb.routes']

package_data = \
{'': ['*'], 'mxcubeweb': ['templates/*']}

install_requires = \
['Flask-Security-Too>=5.0.2,<6.0.0',
 'Flask-SocketIO>=5.3.2,<6.0.0',
 'Flask>=2.2.2,<3.0.0',
 'PyDispatcher>=2.0.6,<3.0.0',
 'bcrypt>=4.0.1,<5.0.0',
 'flask-sqlalchemy>=3.0.2,<4.0.0',
 'gevent-websocket==0.10.1',
 'jsonschema>=4.17.1,<5.0.0',
 'mock>=4.0.3,<5.0.0',
 'mxcube-video-streamer>=1.0.0',
 'mxcubecore>=1.54.0',
 'pydantic>=1.10.2,<2.0.0',
 'pytz>=2022.6,<2023.0',
 'redis>=4.3.5,<5.0.0',
 'ruamel.yaml>=0.17.21,<0.18.0',
 'scandir>=1.10.0,<2.0.0',
 'spectree==1.2.1',
 'tzlocal>=4.2,<5.0',
 'werkzeug==2.3.7']

entry_points = \
{'console_scripts': ['mxcubeweb-server = mxcubeweb:main']}

setup_kwargs = {
    'name': 'mxcubeweb',
    'version': '4.34.0',
    'description': 'MXCuBE Web user interface',
    'long_description': '[![Build and test](https://github.com/mxcube/mxcubeweb/actions/workflows/build_and_test.yml/badge.svg)](https://github.com/mxcube/mxcubeweb/actions/workflows/build_and_test.yml)\n![PyPI](https://img.shields.io/pypi/v/mxcubeweb)\n\n<p align="center"><img src="https://mxcube.github.io/mxcube/img/mxcube_logo20.png" width="125"/></p>\n\n# MXCuBE-Web\n\nMXCuBE-Web is the latest generation of the data acquisition software MXCuBE (Macromolecular Xtallography Customized Beamline Environment). The project started in 2005 at [ESRF](https://www.esrf.eu), and has since then been adopted by other institutes in Europe. In 2010, a collaboration agreement has been signed for the development of MXCuBE with the following partners:\n\n- [ESRF](https://www.esrf.fr/)\n- [Soleil](https://www.synchrotron-soleil.fr/)\n- [MAX IV](https://www.maxiv.lu.se/)\n- [HZB](https://www.helmholtz-berlin.de/)\n- [EMBL](https://www.embl.org/)\n- [Global Phasing Ltd.](https://www.globalphasing.com/)\n- [ALBA](https://www.cells.es/)\n- [DESY](https://www.desy.de/)\n- [LNLS](https://lnls.cnpem.br/)\n- [Elettra](https://www.elettra.eu/)\n- [NSRRC](https://www.nsrrc.org.tw/)\n- [ANSTO](https://www.ansto.gov.au/facilities/australian-synchrotron)\n\nMXCuBE-Web is developed as a web application and runs in any recent browser.\nThe application is built using standard web technologies\nand does not require any third-party plugins to be installed in order to function.\nBeing a web application, it is naturally divided into server and client parts.\nThe communication between the client and server are made using HTTP/HTTPS and web-sockets.\nIt is strongly recommended to use HTTPS, SSL/TLS encrypted HTTP.\nThe traffic passes through the conventional HTTP/HTTPS ports,\nminimizing the need for special firewall or proxy settings to get the application to work.\n\n<img align="center" src="https://mxcube3.esrf.fr/img/client-server.png" width=300>\n\nThe underlying beamline control layer\nis implemented using the library [`mxcubecore`](https://github.com/mxcube/mxcubecore)\npreviously known as [`HardwareRepository`](https://github.com/mxcube/HardwareRepository).\nThe `mxcubecore` library is compatible with\nboth the MXCuBE-Web and the [MXCuBE-Qt](https://github.com/mxcube/mxcubeqt) applications.\n\n|                                                       Data collection                                                       |                                                       Sample grid                                                       |\n| :-------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------: |\n| ![datacollection-view](https://user-images.githubusercontent.com/4331447/42496925-d983bf3e-8427-11e8-890e-898dda649101.png) | ![samplegrid-view](https://user-images.githubusercontent.com/4331447/42496937-e8547b34-8427-11e8-9447-645e6d7f1dc5.png) |\n\nLatest information about the MXCuBE project can be found on the\n[MXCuBE project webpage](https://mxcube.github.io/mxcube/).\n\n## Technologies in use\n\nThe backend is built on the Python [Flask](https://flask.palletsprojects.com/) web framework,\na library called [SocketIO](https://socket.io/) is further used to provide\na bidirectional communication channel between backend and client.\nThe backend exposes a REST API to the client.\n\nThe client is implemented in ECMAScript6 and HTML5.\nReact, Boostrap, and FabricJS are the main libraries used for the UI development.\n\n## Information for developers\n\n- [Contributing guidelines](https://github.com/mxcube/mxcubeweb/blob/master/CONTRIBUTING.md)\n- [Developer documentation](https://mxcubeweb.readthedocs.io/)\n- [Development install instructions](https://mxcubeweb.readthedocs.io/en/latest/dev/environment.html#install-with-conda)\n\n## Information for users\n\n- [User Manual MXCuBE Web](https://www.esrf.fr/mxcube3)\n- [Feature overview](https://github.com/mxcube/mxcubeqt/blob/master/docs/source/feature_overview.rst)\n- If you cite MXCuBE, please use the references:\n  > Oscarsson, M. et al. 2019. “MXCuBE2: The Dawn of MXCuBE Collaboration.” Journal of Synchrotron Radiation 26 (Pt 2): 393–405.\n  >\n  > Gabadinho, J. et al. (2010). MxCuBE: a synchrotron beamline control environment customized for macromolecular crystallography experiments. J. Synchrotron Rad. 17, 700-707\n',
    'author': 'The MXCuBE collaboration',
    'author_email': 'mxcube@esrf.fr',
    'maintainer': 'MXCuBE collaboration',
    'maintainer_email': 'mxcube@esrf.fr',
    'url': 'https://github.com/mxcube/mxcubeweb',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
