# StackLang: Stack memory programming language.

## Description
Simple programming language made in Python.
It simulates a stack memory in numbers and you can code with that.

*Programming language is on development and it could change the commands without advertising.*

## Example
Adding calculator (it receives 2 numbers and return the value of adding)
```
start

input
input

advance
add

get.value

end
```

## Guide
### Instructions
#### Start and Exit
*start* Start the file, sets the pointer 0

*exit* Ends the program.
#### Input and Output
*input* Reads a number from the user

*get.value* Print the value in the current position

*get.position* Print the index of the current position

#### Math
*add* Adds the numbers of the 2 numbers behind the position and creates a new position with the value (the pointer goes to the new position auto)

*sub* Substracts the numbers of the 2 numbers behind the position and creates a new position with the value (the pointer goes to the new position auto)

#### Movement
*advance* Move the pointer to the next position

*back* Move the ponter to the position behind to the current.