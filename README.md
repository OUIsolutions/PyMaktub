# PyMaktube
a Python Library for Procedural Pseudo Randon Generation

### Instalation from pip
```shel 
pip install PyMakTub
```

### Instalation from github

```shel 
pip install git+https://github.com/OUIsolutions/PyMaktube

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
```py
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

### Multiple Generations 
you can generate any itens you want with the same seed 

```py 
from PyMaktube.MakTub import MakTub

r = MakTub("your seed here")

for i in range(0,100):
    print(r.generate_num(0,100))

```

### skping generation 
you also can skip genrations easly 

```py
from PyMaktube.MakTub import MakTub

r = MakTub("your seed here")
r.set_generation(5)# will skip the first 5
for i in range(0,100):
    print(r.generate_num(0,100))
print("generation ",r.get_generation())

```
### Modifiyng the Seed 
its possible to modify the seed , to test diferent results
```py 

from PyMaktube.MakTub import MakTub

r = MakTub("your seed here")
for i in range(0,10):
    r.set_seed(f'test {i}')
    print(r.generate_token())

```

### Making randon seed modifications 

```py


from PyMaktube.MakTub import MakTub
from PyMaktube.MakTubSeqs import MakTubSeqs
r = MakTub("your seed here")
for i in range(0,10):
    r.aply_seed_modification([0,1,2],MakTubSeqs.ALFHA_NUNS)#will modfiy the first 3 chars
    print(r.get_seed())

```