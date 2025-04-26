import os, re
import enum
from utils import balanced

class COMMAND_TYPE(enum.Enum):
    A_COMMAND = 'A_COMMAND'
    C_COMMAND = 'C_COMMAND'
    L_COMMAND = 'L_COMMAND'

class Parser:
    current = None
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
    
    def hasMoreCommand(self) -> bool:
        return self.current < len(self.commands) - 1

    def advance(self) -> None:
        if self.hasMoreCommand:
            self.current += 1
            if self.current == len(self.commands) - 1:
                self.hasMoreCommand = False
            self.currentCommand = self.commands[self.current] 
            print(self.currentCommand + " " + self.commandType().value)
        else:
            return None

    def commandType(self) -> COMMAND_TYPE:
        if "@" in self.currentCommand:
            return COMMAND_TYPE.A_COMMAND
        elif "=" in self.currentCommand:
            return COMMAND_TYPE.C_COMMAND
        elif balanced(self.currentCommand):
            return COMMAND_TYPE.L_COMMAND
        else:
            raise("Invalid Command")