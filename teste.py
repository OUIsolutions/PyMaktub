

from src.PyMaktube.MakTub import MakTub

m = MakTub("f332dd3")
m.aply_seed_modification([0,1,2],"123")
print(m.get_seed())
