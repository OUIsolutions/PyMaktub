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

### Generating a Choice 

```py 
from PyMaktube.MakTub import MakTub

r = MakTub("your seed here")
names = ["Mateus","Samuel","Danilo"]
print(r.choice(names))

```
### Generating tokens 

```py
from PyMaktube.MakTub import MakTub
r = MakTub("your seed here")
size = 10
valid_chars = "ABCDEF"
print(r.generate_token(size,valid_chars))

```

### Probabilitys 
```
from PyMaktube.MakTub import MakTub
r = MakTub("your seed here")
p = r.new_probability()
a = p.add_probability(0.33)
b = p.add_probability(0.33)
c = p.add_probability(0.33)
result = p.perform()
if a  == result:
    print("generated A")
if b == result:
    print("generated B")
if c == result:
    print("generated C")
```

