from setuptools import setup, find_packages

# Leitura do README.md garantindo o fechamento do arquivo
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='PyMakTub',
    version='0.1.2',
    packages=find_packages(where='src'),  # Procurar pacotes no diretório 'src'
    package_dir={'': 'src'},  # Define 'src' como o diretório raiz para pacotes
    include_package_data=True,  # Inclui dados extras como arquivos binários e outros

    package_data={
        '': ['*.py',"*.so","*.dll"],  # Inclui todos os arquivos .py de qualquer pacote
    },

    #ata_files=[('bin', ['src/bin/Maktub.so'])],
    install_requires=[
    ],  # Lista de dependências, adicione conforme necessário
    author='Mateus',
    author_email='mateusmoutinho01@gmail.com',
    description='A Procedural Generation Python Lib',
    long_description=long_description,  # Descrição longa lida do README.md
    long_description_content_type='text/markdown',
    url='https://github.com/seuusuario/seurepositorio',  # Coloque a URL correta do seu repositório Git

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
