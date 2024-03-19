import setuptools

setuptools.setup(
    name='MyGeneratorLatex',
    version='1.1    ',
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    author='Daniil Plotnikov',
    url='https://github.com/OFFdeil/latex_for_homework',
    python_requires='>=3.9',
)