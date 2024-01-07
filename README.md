# Memostacking: Stack memory programming language.

## Description
Simple programming language made in Python.
It simulates a stack memory in numbers and you can code with that.

`python3 Memostacking/interpreter.py program.sl`

*Programming language is on development and it could change the commands without advertising.*

## Example
Adding calculator (it receives 2 numbers and return the value of adding)
```
start

input verbose
input verbose

advance

add
show.current.value verbose

end 
```

## Guide
### Instructions
#### Start and Exit
*start* Start the file, sets the pointer 0

*exit* Ends the program.
#### Input and Output
*input* Reads a number from the user, params: verbose | no.verbose

*show.current.value* Print the value in the current position, params: verbose | no.verbose

*show.current.position* Print the index of the current position, params: verbose | no.verbose

*print* Print a string, params: "string" | "number" (COMPULSORY "")
#### Math
*add* Adds the numbers of the 2 numbers behind the position and creates a new position with the value (the pointer goes to the new position auto)

*sub* Substracts the numbers of the 2 numbers behind the position and creates a new position with the value (the pointer goes to the new position auto)

#### Movement
*advance* Move the pointer to the next position

*back* Move the ponter to the position behind to the current.