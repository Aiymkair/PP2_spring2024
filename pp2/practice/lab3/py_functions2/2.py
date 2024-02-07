from dict_film import movies
def sublist():
    l = [i["name"] for i in movies if i["imdb"] > 5.5]
    return l
print(sublist())
