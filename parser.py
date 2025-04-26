import os, re

class Parser:
    current = 0
    hasMoreCommand = None
    commands = []

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
            print(self.commands)
        except IOError as e:
            print("An Error occurred when opening file", e)
        
        