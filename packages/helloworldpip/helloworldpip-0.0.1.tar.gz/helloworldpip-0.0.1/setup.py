from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Demo Program to Print Hello World'
LONG_DESCRIPTION = 'A demo pip hello world package that will print hello world.'

# Setting up
setup(
    name="helloworldpip",
    version=VERSION,
    author="devsumitg",
    author_email="<devsumitg@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'hello world', 'pip'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)