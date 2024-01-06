import sys

filepath = sys.argv[1] 

# get every line of code
lines = []

with open(filepath, 'r') as f:
    lines = [
        line.strip() for line in f.readlines()
    ]

class Stack:
    def __init__(self, size: int):
        self.buf = [
            0 for _ in range(size)
        ]

        self.sp = -1
        self.running = 0

    def new(self, number):
        self.sp += 1
        self.buf[self.sp] = number

    def delete(self):
        self.buf[self.sp] = 0
        self.sp -= 1

    def getValue(self):
        return self.buf[self.sp]
    
    def advance(self):
        self.sp += 1

    def back(self):
        self.sp -= 1

    def start(self):
        self.sp += 1
        self.running = True

    def exit(self):
        self.running = False

memory = Stack(256)

for line in lines:
    words = line.split(" ")
    token = words[0]

    # start and exit
    if token == "start":
        memory.start()
    elif token == "end":
        memory.exit()
        sys.exit(0)
    
    # input output
    elif token == "input":
        memory.new(int(input("")))
    elif token == "get.value":
        print(str("Value: " + str(memory.getValue())))
    
    # math
    elif token == "add":
        memory.back()
        num1 = memory.getValue()

        memory.back()
        num2 = memory.getValue()

        memory.advance()
        
        memory.new(int(num1) + int(num2))
    elif token == "sub":
        memory.back()
        memory.back()
        num1 = memory.getValue()

        memory.advance()
        num2 = memory.getValue()

        memory.advance()
        memory.new(num1-num2)

    # movement
    elif token == "advance":
        memory.advance()
    elif token == "back":
        memory.back()
    elif token == "get.position":
        print("Position: " + str(memory.sp))