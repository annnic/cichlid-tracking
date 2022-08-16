import os

from setuptools import find_packages, setup

install_requires = [
    line.rstrip()
    for line in open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
]

setup(
    name="cichlid-tracking",
    install_requires=install_requires,
    version="0.0.1",
    description="Recording and online tracking for cichlids",
    url="https://github.com/annnic/cichlid-tracking",
    license="GNU General Public License v3.0",
    packages=find_packages(),
    zip_safe=False,
)