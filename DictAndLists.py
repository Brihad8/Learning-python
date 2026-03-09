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
def dict_interation():
    for i in planets.keys():#the .keys function returns all the keys in the dict.
        print(f"{i} is in order number:{planets[i]} ")# planets[i] gives me the value assosiated with the key

# e.g. planets.values()funcition would only return the value associated with each key, not the key it's self

#Dict methods
# the dict is use to store the name of the coustomer and the issue they are facing
coustomer_support = {
    "userA":"issue1",
    "userB":"issue2",
    "userC":"issue3",
    "userD":"issue4"
}#dict used for the exaples

#.items() returns the key and the value of the key

'''for user,prob in coustomer_support.items():
    print(f"{user} is facing {prob}")'''

#.pop() returns the value of the key and remove the key and the value from the dict

def complete():
    pass
    status = input("enter the status: y for complete, n for not complete")
    user =input("enter user name")
    if status == "y":
        issue = coustomer_support.pop(user)
        return(f"Thx for sloving {issue} for {user}")
        
    else:
        print(f"dont give up")

# As each coustomer's problems are dealt with we can use the .pop() to remove them and their issue from the dict.

#.clear() deletes all the keys and values in the dict
#if all the problem are finished at once 
#coustomer_support.clear() can be used to delete all the values and keys in the dict


#Lists
games = ["GTA5","Pokemon Ruby","Call of Duty","TF2"]

# to add more items , we can use the fuction .append(newitem)]
games.append("Temple run")
# to add more than one item at a time we can use the .extend([newitem1,newitem2])
games.extend(["Csgo","Ow2"])
# to remove and item from the list we can use the .remove fucntion
games.remove("GTA5")
# to add a list to the list we can use the .append fuction again
games.append(["pokemon sun","pokemon moon"])
print(games)