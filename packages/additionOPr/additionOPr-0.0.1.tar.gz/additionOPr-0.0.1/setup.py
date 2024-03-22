import setuptools 

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setuptools.setup( 
    name='additionOPr',   
    version='0.0.1', 
    author="Roqaiah Jamil", 
    author_email="roqaiahjamil96@gmail.com", 
    description="This package provides a function to add two numbers", 
    long_description=readme(),
    long_description_content_type='text/markdown',
    readme = "README.md",
    requires_python = ">=3.8",
    packages=setuptools.find_packages(), 
    classifiers=[ 
    "Programming Language :: Python :: 3", 
    "License :: OSI Approved :: MIT License", 
    "Operating System :: OS Independent", 
    ], 
) 