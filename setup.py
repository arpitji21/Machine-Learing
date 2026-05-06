from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    # this function will return the list of requiremtents
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # in requiremnets.txt at last of each line there is a new line character so we need to remove it.
        requirements = [req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
            
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='arpit',
    author_email='hackhammer404@gmail.com',
    packages = find_packages(),
    install_requires=get_requirements('requirements.txt')

)