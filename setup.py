import setuptools


setuptools.setup(
    name='lolwrapper',
    version='1.0',
    packages=setuptools.find_packages(),
    author='Brian Perrett',
    author_email='perrettbrian@gmail.com',
    description='Riot API Wrapper',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/brianjp93/lolapi",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
