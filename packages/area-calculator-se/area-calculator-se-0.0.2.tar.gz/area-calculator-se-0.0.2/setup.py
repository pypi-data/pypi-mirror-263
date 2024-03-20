import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # This is the name of the package
    name="area-calculator-se",
    # The initial release version
    version="0.0.2",
    # Full name of the author
    author="Saeideh Eslamian",
    description="Calculate areas of geometrical figures",
    # Long description read from the the readme file
    long_description=long_description,
    long_description_content_type="text/markdown",
    # List of all python modules to be installed
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                                      # Information to filter the project on PyPi website
    # Minimum version requirement of the package
    python_requires='>=3.6',
    # Name of the python package
    py_modules=["area_calculator_se"],
    # Directory of the source code of the package
    package_dir={'': 'area-calculator-se/src'},
    # Install other dependencies if any
    install_requires=[]
)
