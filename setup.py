from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="MILES",
    author="https://github.com/Kvasirs",
    description="",
    long_description=__doc__,
    version="0.0.1",
    url="https://github.com/ibot3/MILES",
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    zip_safe=False,
    python_requires=">= 3.5",
    install_requires=required,
    classifiers=[
    ],
)
