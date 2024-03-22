from setuptools import setup, find_packages

# Чтение зависимостей из файла requirements.txt
with open('requirements.txt') as f:
    dependencies = f.read().splitlines()

setup(
    name='ApiTools_for_aiyoloAPI',
    version='0.1',
    packages=find_packages(),
    install_requires=dependencies,
    author='Alex',
    author_email='234iskateli234@gmail.com',
    description='api tools',
    url='https://github.com/Ten-o69/ApiTools_for_aiyoloAPI',
)
