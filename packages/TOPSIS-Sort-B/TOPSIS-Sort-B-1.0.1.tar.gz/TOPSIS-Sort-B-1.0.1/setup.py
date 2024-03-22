from setuptools import setup, find_packages, Extension

VERSION = '1.0.1'
DESCRIPTION = 'Topsis-Sort-B package'

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setup(
    name="TOPSIS-Sort-B",
    version=VERSION,
    author="gilbertomoj",
    author_email="gibamedeirosgc@gmail.com",
    description=DESCRIPTION,
    long_description="",
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