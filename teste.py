

from src.PyMaktube.MakTub import MakTub

m = MakTub("qdueaa porra é melhoroudd agorddda666")
m.set_generation(10000)

for i in range(0,10):
    print(m.generate_token())
