from setuptools import setup, find_packages

setup(
    name='PyMakTub',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,  # Necessário para incluir dados extras

    package_data={
        '': ['*.py'],
        'src/bin': ['src/bin/Maktub.so'],

    },
    install_requires=[],
    author='Mateus',
    author_email='mateusmoutinho01@gmail.com',
    description='An Procedural Generation  Python Lib',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='seu git',  # URL do repositório
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
