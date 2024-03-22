from setuptools import setup, find_packages

# Чтение зависимостей из файла requirements.txt
with open('requirements.txt') as f:
    dependencies = f.read().splitlines()

setup(
    name='TestLib_ruiewuroiew',
    version='0.1',
    packages=find_packages(),
    install_requires=dependencies,
    author='Your Name',
    author_email='your@email.com',
    description='Description of your library',
    url='https://github.com/yourusername/yourrepository',
)
