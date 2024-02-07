#IMDB > 5
from PP2_spring2024.pp2.practice.lab3.py_functions2.dict_film import movies

def check(name = "Joking muck"):
    l = [i["imdb"] for i in movies if i["name"]==name]
    return l[0] > 5.5
print (check())