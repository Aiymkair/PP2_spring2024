from dict_film import movies

def category(category):
    a = [i["imdb"] for i in movies if i["category"] == category]
    return sum(a)/len(a)
