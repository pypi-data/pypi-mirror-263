from setuptools import setup, find_packages

with open('C:/Users/student/VSCode/random_word_gen/README.md','r') as f:
    description = f.read()


setup(
    name='random_word_gen',
    version="0.5.0",
    packages=find_packages(),
    install_requires=[

    ],
    long_description=description,
    long_description_content_type="text/markdown",
)