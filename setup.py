import setuptools
from os import path


BASE = path.abspath(path.dirname(__file__))

with open(path.join(BASE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='lolwrapper',
    version='1.01',
    packages=setuptools.find_packages(),
    install_requires=['requests',],
    author='Brian Perrett',
    author_email='perrettbrian@gmail.com',
    description='Riot API Wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/brianjp93/lolapi",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
