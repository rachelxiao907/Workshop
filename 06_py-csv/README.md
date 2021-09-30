# SUMMATIVE ASSESSMENT
Team Polar - Jesse Xie, Rachel Xiao, Yuqing Wu  
SoftDev   
K06: StI/O: Divine Your Destiny!  
2021-09-29  


## File Input
* To read the file, we first opened the csv file and stored the data in the file as a reader object, where each row was stored as a list and the values in the row were stored as values in that list.
* We then looped through the lists in reader from our csv file (excluding the first row, which was the header) and stored them into the dictionary that we made. The job classes are the keys and the percentages are the corresponding values.

## Dictionaries: What is it good for? How is it used?
* Create a dictionary with DICT = {key:value, key:value, ...}
* A dictionary is used to store data values organized by the name of the key which can hold multiple values as one element because of the key:value pair (like a list of items assigned to a certain key). This is unlike other data structures as you can access a key by putting its name as a parameter of the dictionary DICT["key_name"].
* It's easy to add new keys and values into the dictionary (DICT["new_key"] = value), as well as new values to existing keys.  
* Unlike lists, dictionaries make it easy to access data even when keys and values are added or deleted. Furthermore, the data in dictionaries can be retrieved with whatever data type the key is in (unlike lists which require indexes as integers).
* The dict.keys() method returns all of the keys in the dictionary. The dict.values() function returns all of the values of the dictionary. The dict.items() function returns all of the key:value pairs of the dictionary.
* The keys and the values in the dictionary can looped through for easy access to the data in the dictionary.
* The keys and values in the dictionary that are stored in the dictionary are unordered, meaning that the order that the keys and values are inputted in is insignificant.

## Lists: What is it good for? How is it used?
* Create a list with list = [value, value1, value2, ...]
* A list is used to store values or elements at different indexes that are integers.Only one set of values is needed to create a list.
* To access a value, the particular index is needed (list[index]).
* Unlike dictionaries, the elements in the list are in order.
* Add to a list with the list.append(value) function. Remove from a list with the list.remove(value) function.

## Basics of Github-flavored Markdown
* Markdown is a text-to-HTML conversion tool which allows people to write using an easy-to-read, easy-to-write plain text format. It allows users to style their text easily too! People usually use it to explain the purpose of a program, how to use it, and how the code works.
* "#" creates headings. The more " # ", the smaller the headings get.
* Create lists using " * " or " - " at the beginning of a line followed by a space. Indent the line on the next line to create nested lists.
* " * " around a word with no space around it italicizes it. " ** " around a word with no space bolds it.
* Learning how to use Markdown is very easy as you can just look at other people's Markdown files to learn the syntax. Some basic syntax in markdown is [here](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

## Weighted Randomized Selection
* We generated a random number that was within 0.0 and the total percentage in the csv file.
* We did the weighted percentage part by designating different areas from 0.0 to total percentage to the different occupations depending on the percentage they occupy.
  * ex. 0.0 to 6.0 could be Management, and 6.1 to 11.0 could be Business and Financial Operations if the dictionary is looped through in this order.
* We checked which occupation the random number would "land on", and that would be the occupation we selected.
  * ex. If the random number is 9.0, we would first subtract the Management part from it, making sure that it doesn't land in the Management section, and then subtract the percentage for the Business and Financial Operations from the random number, making it negative, and that means the random number lands in Business and Financial Operations section.
* This is a truly randomized process as the order we loop through the dictionary is random, which means each time different sections may be allocated to the occupations. 
