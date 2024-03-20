import os
from setuptools import setup, find_packages

# Read the contents of your README file
with open(os.path.join(os.getcwd(), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='latexgenerator5233-yoloer',
    version='1.0.2',
    packages=find_packages(),
    py_modules=['latex_generator'],
    install_requires=[],
    python_requires='>=3.7',
    author='Wangquanyu',
    author_email='w1450111904@gmail.com',
    description='A simple LaTeX table and image generator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='LaTeX, table, image, generator',
    url='https://github.com/gdnjr5233/Advanced-Python_2024',
)