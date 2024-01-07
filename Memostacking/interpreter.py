import sys

filepath = sys.argv[1]

program = {
    "size": 256,
    "code": []
}

class Parser:
    def __init__(self):
        self.lines = []

    def getLines(self):
        with open(filepath, 'r') as f:
            self.lines = [
                line.strip() for line in f.readlines()
            ]

    def parse(self):
        for line in self.lines:
            words = line.split(" ")
            token = words[0]

            # start and end
            if token == "start":
                program["code"].append({"type": "START_TOKEN", "params": None})
            if token == "end":
                program["code"].append({"type": "END_TOKEN", "params": None})

            # input and output
            if token == "input":
                # program["code"].append({"type": "INPUT_TOKEN", "params": None})
                if words[1] == "verbose":
                    program["code"].append({"type": "INPUT_TOKEN", "params": {"verbose": True}})
                elif words[1] == "no.verbose":
                    program["code"].append({"type": "INPUT_TOKEN", "params": {"verbose": False}})
                elif not words[1]:
                    program["code"].append({"type": "INPUT_TOKEN", "params": {"verbose": False}})
                else:
                    print("Error: Input command has a unidentified parameter.")
            if token == "show.current.value":
                if words[1] == "verbose":
                    program["code"].append({"type": "SHOWCURRENTVALUE_TOKEN", "params": {"verbose": True}})
                elif words[1] == "no.verbose":
                    program["code"].append({"type": "SHOWCURRENTVALUE_TOKEN", "params": {"verbose": False}})
                elif not words[1]:
                    program["code"].append({"type": "SHOWCURRENTVALUE_TOKEN", "params": {"verbose": False}})
                else:
                    print("Error: show.current.value command has a unidentified parameter.")
            if token == "show.current.position":
                if words[1] == "verbose":
                    program["code"].append({"type": "SHOWCURRENTPOSITION_TOKEN", "params": {"verbose": True}})
                elif words[1] == "no.verbose":
                    program["code"].append({"type": "SHOWCURRENTPOSITION_TOKEN", "params": {"verbose": False}})
                elif not words[1]:
                    program["code"].append({"type": "SHOWCURRENTPOSITION_TOKEN", "params": {"verbose": False}})
                else:
                    print("Error: show.current.position command has a unidentified parameter.")

            if token == "print":
                if len(words) > 1:
                    # Buscamos el índice de la primera comilla
                    start_quote_index = line.find('"')
                    if start_quote_index != -1:
                        # Si encontramos una comilla, buscamos la segunda comilla a partir de ahí
                        end_quote_index = line.find('"', start_quote_index + 1)
                        if end_quote_index != -1:
                            # Extraemos la frase entre comillas
                            value = line[start_quote_index + 1:end_quote_index]
                            program["code"].append({"type": "PRINT_TOKEN", "params": {"value": value}})
                        else:
                            print("Error: Missing closing quote in print command.")
                    else:
                        print("Error: Missing opening quote in print command.")
                else:
                    print("Error: print command requires a parameter.")
            # math
            if token == "add":
                program["code"].append({"type": "ADD_TOKEN", "params": None})
            if token == "sub":
                program["code"].append({"type": "SUBSTRACT_TOKEN", "params": None})
            if token == "mul":
                program["code"].append({"type": "MULTIPLY_TOKEN", "params": None})
            if token == "div":
                program["code"].append({"type": "DIV_TOKEN", "params": None})

            # movement
            if token == "advance":
                program["code"].append({"type": "ADVANCE_TOKEN", "params": None})
            if token == "back":
                program["code"].append({"type": "BACK_TOKEN", "params": None})

# memory stack
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

# interpreter
class Interpreter:
    def __init__(self, program, memory: Stack) -> None:
        self.program = program
        self.memory = memory

    def run(self):
        for token_info in program["code"]:
            token_type = token_info["type"]
            if token_type == "START_TOKEN":
                self.memory.start()
            if token_type == "END_TOKEN":
                self.memory.exit()

            if token_type == "INPUT_TOKEN":
                # self.memory.new(int(input()))
                if token_info["params"]["verbose"] == True:
                    self.memory.new(int(input("Input> ")))
                elif token_info["params"]["verbose"] == False:
                    self.memory.new(int(input()))
            if token_type == "SHOWCURRENTVALUE_TOKEN":
                if token_info["params"]["verbose"] == True:
                    print(str("Current value: " + str(self.memory.buf[self.memory.sp])))
                elif token_info["params"]["verbose"] == False:
                    print(str(self.memory.buf[self.memory.sp]))
            if token_type == "SHOWCURRENTPOSITION_TOKEN":
                # print(str(self.memory.sp))
                if token_info["params"]["verbose"] == True:
                    print(str("Current position: " + str(self.memory.sp)))
                elif token_info["params"]["verbose"] == False:
                    print(str(self.memory.sp))
            if token_type == "PRINT_TOKEN":
                print(str(token_info["params"]["value"]).strip('\'"'))

            if token_type == "ADD_TOKEN":
                self.memory.back()
                num1 = self.memory.getValue()

                self.memory.back()
                num2 = self.memory.getValue()

                self.memory.advance()

                self.memory.new(int(num1) + int(num2))
            if token_type == "SUBSTRACT_TOKEN":
                self.memory.back()
                num2 = self.memory.getValue()

                self.memory.back()
                num1 = self.memory.getValue()

                self.memory.advance()

                self.memory.new(int(num1) - int(num2))

            if token_type == "ADVANCE_TOKEN":
                self.memory.sp += 1
            if token_type == "BACK_TOKEN":
                self.memory.sp -= 1

memory = Stack(256)
parser = Parser()
parser.getLines()
parser.parse()
interpreter = Interpreter(program, memory)
interpreter.run()