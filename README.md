# PyMaktube
a Python Library for Procedural Pseudo Randon Generation

Instalation,for instalation just type:

```shel 
pip install git+https://github.com/mateusmoutinho/PyMaktube

```

### Quick Usage 
For making anything on Maktub , first you need to setup a seed, than you can generate
numbers, itens ,choices , etc

### Generating a Number
```py
from PyMaktube.MakTub import MakTub

r = MakTub("your seed here")
print(r.generate_num(0,100))

```

