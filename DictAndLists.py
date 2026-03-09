#Dict 

#genral syntax to create a dictionary

fruits = {"apple":"red","banana":"yellow","avocado":"green"}

# Adding another item

fruits["orange"] = "orange"

# adding multiple keys

fruits.update({"pine apple":"yellow","kiwi":"light brown"})

# function to find the colour of any fruit which is in the dict, if it is not present it returns unknown.

def colourReturn():
    pass # only here to stop this fucnction from interferaing in other tests
    fruit = input("Enter name of fruit: ") 
    return fruits.get(fruit,"unknown")

'''run = colourReturn()
print(run)'''

'''Example outputs for colourReturn function
1)
Enter name of fruit: apple
red
since apple is a key present in fruits, it returns the value associated with the key apple
2)
Enter name of fruit: mango
unknown
mango is not a key in the fruits, hence it returns unknown
3)
Enter name of fruit: kiwi
light brown
'''

#planets and their order number
planets = {
    "Mercury":1,
    "Venus":2,
    "Earth":3,
    "Mars":4,
    "Jupiter":5,
    "Saturn":6,
    "Uranus":7,
    "Neptune":8

}# writng it outlike this improves readability

#iterating over the dict
for i in planets.keys():#the .keys function returns all the keys in the dict.
    print(f"{i} is in order number:{planets[i]} ")
