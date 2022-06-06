from setuptools import setup, find_packages

setup(
    name='packagetest',
    version='1.0.0',
    author='Carlos Ramirez',
    author_email='charlosrmz_07@hotmail.com',
    package_dir={'packagetest': 'packagetest'},
    packages=find_packages(),
    package_data={'packagetest': []},
    scripts=[],
    url='https://github.com/cramg/Package_Test',
    download_url ='https://github.com/cramg/Package_Test',
    license='MIT',
    description="Esta es una prueba de implementacion de una libreria en Python",
    long_description="Esta libreria es el producto final de un tutorial sobre cómo programar una\
    librería en Python, haciendo ejercicios basicos y replicando el repositorio de Morsa (UIBCDF)",
)
