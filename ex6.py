types_of_people = 10 # Sets a variable "types_of_people"= 10
x = f"There are {types_of_people} types of people." # Sets variable x to a string with an embeded variable

binary = "binary" # Sets variable "binary" to "binary"
do_not = "don't" # Sets variable "do_not" to "don't"
y = f"Those who know {binary} and those who {do_not}." # Sets variable y to string with two embeded format strings

print(x) # Prints x
print(y) # Prints y

print(f"I said: {x}") # Prints variable x embeded in a string
print(f"I also said: '{y}'") # Prints variable y embeded in a string which calls the value of the variable "binary" and "do_not"

hilarious = False # Sets a variable "hilarious"= False
joke_evaluation = "Isn't that joke so funny?! {}" # Sets a variable "joke_evaluation" to a string with an embeded empty format string.

print(joke_evaluation.format(hilarious)) # Prints the content of the variable "joke_evaluation" and after the content of the format string through variable "hilarious" which value is False

w = "This is the left side of..." # Sets a variable w which value is a string
e = "a string with a right side." # Sets a variable w which value is a string

print(w + e) # Prints the sum/concatenation of the variable "w" with "e"

#Study Drills
#1. Go through this program and write a comment above each line explaining it. 
#2. Find all the places where a string is put inside a string.
#3. Are you sure there are only four places? How do you know? Maybe I like lying. 
#4. Explain why adding the two strings w and e with + makes a longer string.
