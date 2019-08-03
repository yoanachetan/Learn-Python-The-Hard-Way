formatter = "{} {} {} {}" # Create a string format and assign the variable formatter

print(formatter.format(1,2,3,4)) # Insert the integers 1,2,3,4 into the string format and print it
print(formatter.format("one", "two", "three", "four")) # Insert the strings "one", "two", "three", "four" and print it
print(formatter.format(True, False, False, True)) # Insert booleans into the string format and print
print(formatter.format(formatter, formatter, formatter, formatter)) # Insert  the format into the string and display it
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
)) # Insert the strings into the format and print it

# Study Drills
# Repeat the Study Drill from Exercise 7.
