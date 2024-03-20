from setuptools import find_packages, setup, Extension

with open('README.md', 'r')as f:
    long_desc = f.read()

setup(
    name='SetCalcPy',
    version='1.2.2',
    description='A library for performing basic set theory operations.',
    package_dir = {'':"src"},
    packages = find_packages(where='src'),
    keywords=['calculator', 'homework-help', 'set-theory'],
    long_description = long_desc,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/SockRocks/Python-Elementary-Set-Theory-Calculator',
    author = 'Ethan Gaver',
    author_email = 'ethaneggcode@gmail.com',
    license = 'GNU',
    extras_require = {
        "dev":["twine >= 4.0.2"]
        },
    python_requires=">=3.11.5"
)
