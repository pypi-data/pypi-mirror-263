import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="point_utils_pxo",
    version="0.1.1",
    author="leehiking",
    author_email="gz6201347@163.com",
    description="test first package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/leehiking/my_pkg_1",
    packages=setuptools.find_packages(),
    install_requires=['torch>=1.0', 'numpy>=1.0'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)