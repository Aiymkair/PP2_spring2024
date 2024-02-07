from dict_film import movies

def avg(l):
    a = [i["imdb"] for i in movies if i["name"] in l]
    return sum(a)/len(l)

print(avg(["Bride Wars", "Love", "Exam", "The Help", "We Two", "Hitman"]))