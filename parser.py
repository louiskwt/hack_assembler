import os, re

class Parser:
    current = None
    hasMoreCommand = None
    commands = []
    currentCommand = None

    def __init__(self, path=None):
        if path is not None:
            self.path = os.path.dirname(__file__) + "/" + path
        else:
            fileName = input("Enter a file path: ")
            self.path = os.path.dirname(__file__) + "/" + fileName
        
        try:
            with open(self.path) as f:
                for line in f:
                    command = line.strip()
                    command = re.sub("\/\/.*", '', command)
                    if command:
                        self.commands.append(command)
            self.hasMoreCommand = True
            self.current = -1
        except IOError as e:
            print("An Error occurred when opening file", e)
    
    def advance(self):
        if self.hasMoreCommand:
            self.current += 1
            if self.current == len(self.commands) - 1:
                self.hasMoreCommand = False
            self.currentCommand = self.commands[self.current] 
            print(self.currentCommand)
        else:
            return None 