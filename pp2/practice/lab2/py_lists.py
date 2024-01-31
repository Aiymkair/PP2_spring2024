#ex1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#banana

#ex2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
#apple changed to kiwi

#ex3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
#["apple", "banana", "cherry", "orange"]-now list looks like this

#ex4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
#["apple", "lemon", "banana", "cherry"]-now list looks like this

#ex5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#["apple", "cherry"]-now list looks like this

#ex6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#cherry

#ex7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
# cherry orange kiwi

#ex8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
