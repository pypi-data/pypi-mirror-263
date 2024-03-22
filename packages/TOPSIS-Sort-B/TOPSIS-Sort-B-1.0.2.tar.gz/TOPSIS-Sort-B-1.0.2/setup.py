from setuptools import setup, find_packages, Extension

VERSION = '1.0.2'
DESCRIPTION = 'Topsis-Sort-B package'

with open("LONG_DESCRIPTION.txt", "r") as fh:
    long_description = fh.read()

setup(
    name="TOPSIS-Sort-B",
    version=VERSION,
    author="gilbertomoj",
    author_email="gibamedeirosgc@gmail.com",
    description=DESCRIPTION,
    long_description=open("README.md", 'r').read(),
    long_description_content_type='text/markdown',
    packages=["TOPSIS-Sort-B"],
    install_requires=["numpy"],
    keywords=['python', 'topsis', 'topsis-sort-b'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
