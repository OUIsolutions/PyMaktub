

from src.PyMaktube.MakTub import MakTub

m = MakTub("qdueaa porra é melhoroudd agorddda666")
x = m.new_probability()
c1 = x.add_probability(0.1)
c2  = x.add_probability(0.9)
for i in range(0,10):
    result = x.perform()

    if c1 == result:
        print("chamou o c1",c1)
    if c2 == result:
        print("chamou o c2",c2)
