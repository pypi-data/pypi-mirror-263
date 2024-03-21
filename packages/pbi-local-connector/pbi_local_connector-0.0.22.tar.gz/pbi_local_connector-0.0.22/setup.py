from setuptools import setup, find_packages

def getVersion(incrementVersion = False) -> str:
    with open("currentVersion.txt") as f:
        version = f.readline()
    
    if incrementVersion:
        with open("currentVersion.txt", mode="w") as f:
            s = version.split(".")
            version = f"{s[0]}.{s[1]}.{int(s[2]) + 1}"
            f.write(version)

    return version


setup(
    name="pbi_local_connector",
    version=getVersion(True),
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    description = "Provides utilities to read data from PowerBI dataset open locally",
    author="ARM",
    url="https://github.com/Alexandre-RM/pbi_local_connector",
    install_requires=["pandas", "pyadomd"]
)

#py setup.py sdist bdist_wheel
#twine upload --skip-existing dist/*

