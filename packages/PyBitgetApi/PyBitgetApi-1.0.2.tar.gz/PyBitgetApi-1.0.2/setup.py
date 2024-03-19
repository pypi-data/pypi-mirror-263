import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyBitgetApi",
    version="1.0.2",
    description="Api Bitget package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={'': '.'},
    packages=setuptools.find_packages(where='.'), 
    install_requires=[
        "loguru",
        "requests",
        "websocket-client"
    ],
)
