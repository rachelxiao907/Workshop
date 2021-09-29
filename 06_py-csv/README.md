# SUMMATIVE ASSESSMENT
Team Polar - Jesse Xie, Rachel Xiao, Yuqing Wu
SoftDev
K06: StI/O: Divine Your Destiny!
2021-09-29


## File Input
* To read the file, we first opened the file and stored the data in the file as a reader object, where each row was stored as a list and the values in the row were stored as values in that list.
* We then looped through the lists in reader from our csv file and stored them into the dictionary that we made. The job classes are the keys and the percentages are the corresponding values.

## Dictionaries: What is it good for? How is it used?
* Create a dictionary with DICT = {key:value, key:value, ...}
* A dictionary is used to store data values organized by the name of the key which can hold multiple values as one element because of the key:value pair (like a list of items assigned to a certain key). This is unlike other data structures as you can access a key by putting its name as a parameter of the dictionary DICT["key_name"]. 
* It's easy to add new keys and values into the dictionary (DICT["new_key"] = value), as well as new values to existing keys.  
* Unlike lists, dictionaries make it easy to access data even when keys and values are added or deleted.
* The dict.keys() method returns all of the keys in the dictionary. The dict.values() function returns all of the values of the dictionary. The dict.items() function returns all of the key:value pairs of the dictionary.
* The keys and the values in the dictionary can looped through for easy access to the data in the dictionary.
* The keys and values in the dictionary that are stored in the dictionary are unordered, meaning that the order that the keys and values are inputted is insignificant.

## Lists: What is it good for? How is it used?
* Create a list with list = [value, value1, value2, ...]
* A list is used to store values or elements at different indexes that are integers.Only one set of values is needed to create a list.
* To access a value, the particular index is needed (list[index]).
* Compared to dictionaries, the elements in the list are in order.
* Add to a list with the list.append(value) function. Remove from a list with the list.remove(value) function.

## Basics of Github-flavored Markdown

## Weighted Randomized Selection
* We generated a random number that was within 0 and the total percentage in the csv file.
