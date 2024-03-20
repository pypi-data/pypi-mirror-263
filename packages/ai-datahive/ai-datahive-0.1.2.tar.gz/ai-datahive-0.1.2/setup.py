from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt') as f:
        return [line.strip() for line in f.readlines() if not line.startswith('#')]


setup(
    name='ai-datahive',
    version='0.1.2',
    packages=find_packages(),
    package_data={
        'transformers': ['templates/*.html'],
        'services': ['prompts/*.txt'],
    },
    description='ETL Package for crawling data, transform it with AI and store it in a datastorage.',
    author='Danny Gerst',
    author_email='d.gerst@bizrock.de',
    install_requires=read_requirements(),
)
