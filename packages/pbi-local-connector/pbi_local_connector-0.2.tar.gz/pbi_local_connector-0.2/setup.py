from setuptools import setup, find_packages

setup(
    name="pbi_local_connector",
    version="0.2",
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)

#py setup.py sdist bdist_wheel