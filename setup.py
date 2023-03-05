from setuptools import find_packages,setup
from typing import List

Hypen_e_dot='-e .'

def get_requirements(find_path:str)->List[str]:
    '''
    this function will returns a list of requiremnts

    '''
    requirements=[]
    with open(find_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)

    return requirements


setup (
name='ML Projects',
version='0.0.1',
author='Rehman',
author_email='rehmanelixir18@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')



)