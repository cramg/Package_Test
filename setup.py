import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
        name="Package Test",
        version="0.0.1",
        author="Carlos Ramirez",
        author_email="charlosrmz_07@hotmail.com",
        description="Ejemplo de implementacion de libreria",
        url="https://github.com/cramg/Package_Test",
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        package_dir={"": "src"},
        packages=setuptools.find_packages(where="src"),
)        
