from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT='-e .'   # '-e .' used in requirements.txt to identify the setup.py to execute.
                     # But we dont need this -e. in setup.py so we remove it.

def get_requirements(file_path:str)->List[str]:
    #this function returns the list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    #Meta data info regarding entire project
    name='ML Project',
    version='0.0.1',
    author='Sudhakar Reddy',
    author_email='tsudhakarreddy@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
