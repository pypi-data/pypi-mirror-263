from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='pro-video-ferramentasdsl',
    version=1.0,
    description='Este pacote fornece ferramentas de processamento de vídeo',
    long_description=Path('README.md').read_text(),
    author='Denis',
    author_email='denis@gmail.com',
    keywords=['camera', 'video', 'processamento'],
    packages=find_packages()  # quando a pessoa roda o pip install e o nome
    # meu módulo ele irá automaticamente instalar todas as dependências que meu
    # pacote precisa
)
