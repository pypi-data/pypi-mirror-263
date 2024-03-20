import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.2'
PACKAGE_NAME = 'cnp_make'
AUTHOR = 'Ivan Perez Louzan'
AUTHOR_EMAIL = 'iperez@coninpe.es'
URL = 'https://github.com/linuxivan'

LICENSE = 'GPLv3'
DESCRIPTION = 'Crea la estructura principal para el desarrollo de nuevos modulos'
LONG_DESCRIPTION = (HERE / "README.md").read_text(
    encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
    'argparse',
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'cnp_make = cnp_make.cli:main'
        ]
    }
)
