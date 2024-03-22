import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.11'
PACKAGE_NAME = 'Andreani_QA_Scanner'  # Debe coincidir con el nombre de la carpeta
AUTHOR = 'AndreaniTesting'
AUTHOR_EMAIL = 'user_appglatest@andreani.com'
URL = ''
LICENSE = 'MIT'  # Tipo de licencia
DESCRIPTION = 'SeleniumFramework para ejecución de casos automatizados'  # Descripción corta
LONG_DESCRIPTION = ""
LONG_DESC_TYPE = "text/markdown"

# Paquetes necesarios para que funcione la librería.
INSTALL_REQUIRES = ['blinker == 1.7.0', 'bottle == 0.12.25', 'clr-loader == 0.2.6', 'Flask == 3.0.0',
                    'Flask-Cors == 4.0.0',
                    'libretranslatepy == 2.1.1', 'mtranslate == 1.8', 'openpyxl == 3.1.2', 'pillow == 10.2.0',
                    'proxy-tools == 0.1.0',
                    'pynput == 1.7.6', 'PySocks == 1.7.1', 'pythonnet == 3.0.1', 'pywebview == 4.3.3',
                    'requests == 2.31.0',
                    'requests-file == 1.5.1', 'screeninfo == 0.8.1', 'selenium == 4.11.2', 'trio == 0.22.2',
                    'trio-websocket == 0.10.3']

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
    package_data={
        'Andreani_QA_Scanner': ['app/*.js', 'app/extension/*.css', 'app/extension/*.png', 'app/extension/*.js',
                                'app/extension/*.html', 'app/extension/*.svg', 'app/extension/*.json',
                                'app/src/*.json', 'src/*.js', 'src/js/*.json', 'src/js/*.js', 'src/style/*.css',
                                'src/templates/*.html']},
    include_package_data=True
)
