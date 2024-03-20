from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='ferramentas_pro_camera',
    version=1.0,
    description='Este pacote irá fornecer ferramentas de processamento de video',
    long_description=Path('README.md').read_text(),
    author='Diogo Jesus',
    author_email='diogojesus.nascimento@outlook.com',
    keywords=['Camera', 'Video', 'Processamento'],
    packages=find_packages()
)