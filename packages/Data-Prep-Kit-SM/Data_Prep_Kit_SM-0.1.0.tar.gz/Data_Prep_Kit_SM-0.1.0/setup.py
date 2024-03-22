from setuptools import setup, find_packages

setup(
    name='Data_Prep_Kit_SM',
    version='0.1.0',
    description='A Python package for data preprocessing tasks',
    author='Sama',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy'
    ],
    python_requires='>=3.10',
)