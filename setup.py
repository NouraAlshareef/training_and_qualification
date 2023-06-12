from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in training_and_qualification/__init__.py
from training_and_qualification import __version__ as version

setup(
	name="training_and_qualification",
	version=version,
	description="Training and Qualification Department for Employees at Sana\'a University - Presidency of the University - Administrative Affairs",
	author="NouraAlshareef",
	author_email="eng.nouraalshareef98@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
