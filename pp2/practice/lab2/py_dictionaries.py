#ex1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#Mustang

#ex2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"]= 2020 
#year:2020

#ex3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"
# brand: Ford,
# model: Mustang
# year: 1964
# color: red

#ex4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")


#ex5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()