import setuptools
import subprocess
import os

remote_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

if "-" in remote_version:
    # when not on tag, git describe outputs: "1.3.3-22-gdf81228"
    # pip has gotten strict with version numbers
    # so change it to: "1.3.3+22.git.gdf81228"
    # See: https://peps.python.org/pep-0440/#local-version-segments
    v,i,s = remote_version.split("-")
    remote_version = v + "+" + i + ".git." + s

assert "-" not in remote_version
assert "." in remote_version

assert os.path.isfile("nestedfunctions/version.py")
with open("nestedfunctions/VERSION", "w", encoding="utf-8") as fh:
    fh.write(f"{remote_version}\n")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


# this grabs the requirements from requirements.txt
required_libs = {"pyspark"}
REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines() if i.split("==")[0] in required_libs]


setuptools.setup(
    name="pyspark_nested_functions",
    version=remote_version,
    author="Brend Braeckmans <brend@distilleddata.be>, Egor Goloshchapov <golosegor@gmail.com>",
    description="Utility functions to manipulate nested structures using pyspark",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/golosegor/pyspark-nested-fields-functions",
    packages=setuptools.find_packages(exclude=["tests"]),
    package_data={"nestedfunctions": ["VERSION"]},
    include_package_data=True,
    # We make use of annotations which is only supported from python 3.7 onwards and Python 3.12 is not supported on Spark 3.5.0 yet
    python_requires=">=3.7, <3.12",
    install_requires=[
        REQUIREMENTS
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)