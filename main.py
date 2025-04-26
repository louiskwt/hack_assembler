from parser import Parser, COMMAND_TYPE

def main():
    print("Hack Assembler")
    p = Parser("Add.asm")
    while p.hasMoreCommand:
        p.advance()
        if p.currentCommandType == COMMAND_TYPE.A_COMMAND.value:
            print(p.symbol())
        elif p.currentCommandType == COMMAND_TYPE.C_COMMAND.value:
            print(p.dest())
            print(p.comp())
            print(p.jump())
        elif p.commandType == COMMAND_TYPE.L_COMMAND.value:
            print(p.symbol())

if __name__ == "__main__":
    main()