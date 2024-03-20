# a setup.py file for my package named shorse to upload to pypi

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='shorse',
    version='0.0.2',
    description='A package to display a shorse',
    url='',
    author='Shorse',
    author_email='yusufy2004@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=requirements,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
)
