from setuptools import setup,find_packages
from typing import List



PROJECT_NAME = "movie-grossincome-prediction"
VERSION = "0.0.0.1"
AUTHOR = "Group 1"
DESCRIPTION = "This is the first group project of 2023 Ai and Data science"
PACKAGES = ["Movies"]
REQUIREMENTS_FILE = "requirements.txt"


def get_requirements_list() ->List[str]:
    """
    Description: This function will return the List of libraries 
    that has to be installed.
    """
    with open (REQUIREMENTS_FILE) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
    name = PROJECT_NAME,
    version= VERSION,
    author= AUTHOR,
    description= DESCRIPTION,
    packages= PACKAGES,
    install_requires = get_requirements_list()
)