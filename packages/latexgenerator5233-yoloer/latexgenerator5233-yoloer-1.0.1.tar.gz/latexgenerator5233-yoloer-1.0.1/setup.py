import os
from setuptools import setup, find_packages

# Read the contents of your README file
with open(os.path.join(os.getcwd(), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='latexgenerator5233-yoloer',  # Название вашей библиотеки
    version='1.0.1',  # Версия библиотеки
    packages=find_packages(),  # Автоматически находит пакеты в вашем проекте
    install_requires=[],  # Зависимости, необходимые для работы вашей библиотеки
    python_requires='>=3.6',  # Минимальная версия Python
    author='Wangquanyu',  # Ваше имя
    author_email='w1450111904@gmail.com',  # Ваш email
    description='A simple LaTeX table and image generator',
    long_description=long_description,
    # This is important for markdown files
    long_description_content_type='text/markdown',
    keywords='LaTeX, table, image',
    url='https://github.com/gdnjr5233/Advanced-Python_2024',  # Ссылка на репозиторий проекта
)