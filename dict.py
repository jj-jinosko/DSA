# exploring mapping types in python

# reference video for defaultdict
# https://www.youtube.com/watch?v=sunYwbKAzI0&ab_channel=anthonywritescode

# dictionaries (key:value pairs)
    # sets keys

# collections library, modifies existing collection data types (dict, list, tuple) {}, (), []
    # defaultdict


myDict = {"a": "apple", "b": "banana", "c": "cantaloupe", "d": "dragon fruit"}
mySet = {"a", "b", "c", "d"}

def loopDict(dict):
    for key in dict:
        print(key) # get keys
        print(dict[key]) # get values of keys

def getDictKey(dict):
    # print(dict["e"]) # KeyError: 'e'
    print(dict.get("e")) # returns None
    print(dict.get("e", "elderberry"))
    # does that mean elderberry was added to myDict? NO!!!! this was a trick
    print(dict)

#-----------------------------------------------------------------
# get does not modify the dict, .setdefault() does modify it!
#-----------------------------------------------------------------
    
import collections as c
## defaultdict
# provide default value! based on value factory?

myDDict = c.defaultdict(int)
myDDict["a"] = "anteater"
print(myDDict["a"])
print(myDDict["b"])

# so, how does this differ from using .get()?
# let's say I want to have a count for the letters

# for a regular dict, I have to check if the key exists first
# myDict["e"] = myDict.get("e", 0) + 1 
# print("count regular dictionary", myDict)

# if "f" in myDict:
#     print("blah")
# else:
#     print("boo")

# # myDDict["e"] = myDDict["e"] + 2
# myDDict["e"] += 2
# print("count defaultdict", myDDict)

# if "f" in myDDict:
#     print("blah")
# else:
#     print("boo")

# if key doesn't exist, default dict creates key and assigns it according to the input fn

# print('\n convert map to countries w list of cities')
cities_by_country = {
    'San Mateo': 'US',
    'Toronto': 'CA',
    'Detroit': 'US',
    'London': 'UK',
    'Paris': 'FR',
    'Seattle': 'US',
    'Vancouver': 'CA'
}

def groupCitiesInCountry(dict):
    countryDict = {}
    # for key in dict:
    #     if dict[key] in countryDict:
    #         countryDict[dict[key]].append(key)
    #     else:
    #         countryDict[dict[key]] = [key]


    for city, country in dict.items():
        if country in countryDict:
            countryDict[country].append(city)
        else:
            countryDict[country] = [city]

    # for key in dict:
    #     countryDict[dict[key]] = countryDict.get(dict[key], [key])
    #     print(type(countryDict.get(dict[key], [key])))
            
    for cities_list in countryDict.values():
        cities_list.sort()
    
    return countryDict 

    
# print(groupCitiesInCountry(cities_by_country))

def groupCitiesWDD(cities_by_country):
    dct = c.defaultdict(list)
    for city, country in cities_by_country.items():
        dct[country].append(city)

    for value in dct.values():
        print(value)
    
    return dct

# print(groupCitiesWDD(cities_by_country).values()) 


myDict = {"ap": ["grape", "apple", "apricot"], "berry": ["strawberry", "blueberry", "raspberry"]}

# for value in myDict.values():
#     print(value)
#     value.sort()
#     print(value)

# print(myDict.values())
# for fruits in myDict.values():
#     print(fruits)


# myDict["ap"].sort()
# print(myDict)


# dictItems = myDict.items()
# print(dictItems)

# for x, y in dictItems:
#     print("x, y")
#     print(x, y)

# bigList = (("lvl1", ('ap', ['apple', 'apricot', 'grape']), "zzzzzz"), (("lvl2", ('berry', ['strawberry', 'blueberry', 'raspberry']), "zzzz")))

# print(bigList)

# for x,y,z in bigList:
#     print(x,y,z)


# So, let's recap:

def recap(to_remix):
    new_map = {}
    for city, country in to_remix.items():

        ## if/else version
        # if country in new_map:
        #     new_map[country].append(city)
        #     # new_map[country] = new_map[country].append(city) ## append does not return a value, it just modifies, that's why this doesn't work
        #     # new_map[country] = new_map[country] + [city] # concatenate lists
        # else:
        #     new_map[country] = [city]

        #setdefault() version (like get(), but actually assigns key to default value)
        new_map.setdefault(country, []).append(city)

    # for cities in new_map.values():
    #     cities.sort()

    return new_map

print(recap(cities_by_country))




# playing with dictionaries

penipope = {"tv": [1, 2, 3], 4: "this is a tragedy"}

# access
print(penipope["tv"])
print(penipope.keys())
print(penipope.values())
print(penipope.items())
## access and/or check if key exists
print(penipope.get("tv", "oops"))
if "tv" in penipope:
    print("tv key is in penipope")

# change
penipope["tv"] = "television set"
print(penipope["tv"])
penipope.update({4: "this is not a tragedy"})
print(penipope)

# add items
# ref key
# .update()

# remove items
# del can delete whole dictionary
# del can delete an item from the dictionary 
# del thisdict["model"]
# .pop(key)
# .popitem() # removes last item that was added

# loop through a dictionary
print("\n")
for key in penipope:
    print(f"key: {key}, item: {penipope[key]}") 
    # print(key)

# by default the loop goes through the keys of the dict
# but it can also be done this way
for key in penipope.keys():
    print(key)

print("values")
for value in penipope.values():
    print(value)

for item in penipope.items():
    print(f"item: {item}")
    print("item: {}".format(item)) #ugh, look at that terrible syntax "".format() wth is that xP


# loop through keys AND values with items()
print("keys and items at the same time!")
for key, item in penipope.items():
    print(key, item)

#

# print(enumerate(penipope))
# print(penipope)



