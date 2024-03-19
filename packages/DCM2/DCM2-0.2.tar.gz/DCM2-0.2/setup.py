from setuptools import setup, find_packages

setup(
    name='DCM2',
    version='0.2',
    packages=find_packages(),
    license='MIT',
    author='Axel Osses, Emir Chacra',
    install_requires=[
        'numpy',
        'graphviz',
        'matplotlib'
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)