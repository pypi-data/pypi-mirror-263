from setuptools import find_packages, setup

setup(
    name="python-inflector",
    version="0.0.12",
    description="The Inflector is used for getting the plural and singular form of nouns",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    author="Kemok",
    license="MIT",
    python_requires=">=3.10",
)