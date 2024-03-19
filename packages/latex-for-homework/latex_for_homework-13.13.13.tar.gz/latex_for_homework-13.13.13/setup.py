import setuptools

setuptools.setup(
    name='latex_for_homework',
    version='13.13.13',
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    author='Daniil Plotnikov',
    url='https://github.com/OFFdeil/latex_for_homework',
    python_requires='>=3.9',
)