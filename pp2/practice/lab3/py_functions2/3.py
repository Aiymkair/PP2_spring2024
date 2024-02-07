from dict_film import movies

def c(category = "Thriller"):
    l = [i['name'] for i in movies if i['category']==category]
    return l

print(c())