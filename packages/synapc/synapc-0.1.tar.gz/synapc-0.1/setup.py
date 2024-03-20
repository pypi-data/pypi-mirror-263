
from setuptools import setup, find_packages
 
setup(
    name='synapc', 
    version='0.1',  
    author='Nagaraj Poojari',
    author_email='np137270@email.com',
    description='A minimalistic neural network library in C',
    long_description='',
    long_description_content_type='text/markdown',
    url='https://github.com/nagarajRPoojari/SynapC', 
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
