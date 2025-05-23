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
    currentCommand, currentCommandType = None, None
    line_count = 0
    
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
        return None

    def commandType(self) -> COMMAND_TYPE:
        if "@" in self.currentCommand:
            self.currentCommandType = COMMAND_TYPE.A_COMMAND.value
            return COMMAND_TYPE.A_COMMAND
        elif "=" in self.currentCommand or ";" in self.currentCommand:
            self.currentCommandType = COMMAND_TYPE.C_COMMAND.value
            return COMMAND_TYPE.C_COMMAND
        elif balanced(self.currentCommand):
            self.currentCommandType = COMMAND_TYPE.L_COMMAND.value
            return COMMAND_TYPE.L_COMMAND
        else:
            raise("Invalid Command")
    
    def symbol(self) -> str:
        if self.currentCommandType == COMMAND_TYPE.A_COMMAND.value:
            return self.currentCommand.split("@")[1]
        if self.currentCommandType == COMMAND_TYPE.L_COMMAND.value:
            return re.search('\(([^)]+)', self.currentCommand).group(1)
        else:
            return ""
    
    def dest(self) -> str:
        if self.currentCommandType == COMMAND_TYPE.C_COMMAND.value and "=" in self.currentCommand:
            return self.currentCommand.split("=")[0].strip()
        else:
            return ""
    
    def comp(self) -> str:
        if self.currentCommandType == COMMAND_TYPE.C_COMMAND.value and "=" in self.currentCommand:
            return self.currentCommand.split("=")[1].strip()
        if self.currentCommandType == COMMAND_TYPE.C_COMMAND.value and ";" in self.currentCommand:
            return self.currentCommand.split(";")[0].strip()
        return self.currentCommand
    
    def jump(self) -> str:
        if self.currentCommandType == COMMAND_TYPE.C_COMMAND.value and ";" in self.currentCommand:
            return self.currentCommand.split(";")[1].strip() if ";" in self.currentCommand else ""
    
    def restart(self) -> None:
        self.current = -1
        self.hasMoreCommand = True
    
    def next_line(self, skip: bool = False):
        self.line_count += -1 if skip else 1
