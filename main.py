from parser import Parser, COMMAND_TYPE
from code_generator import CodeGenerator

def main():
    print("Hack Assembler")
    file_name = "Add.asm" 
    p = Parser(file_name)
    code = CodeGenerator()
    out = open(file_name.split(".")[0] + ".hack", "+w")

    while p.hasMoreCommand:
        p.advance()
        if p.currentCommandType == COMMAND_TYPE.A_COMMAND.value:
            address = p.symbol()
            out.write("{0:016b}".format(int(address)))
        elif p.currentCommandType == COMMAND_TYPE.C_COMMAND.value:
            dest_code = p.dest()
            dest = code.dest(dest_code if dest_code else "null")  
            comp = code.comp(p.comp())
            jmp_code = p.jump() 
            jmp = code.jump(jmp_code if jmp_code else "null")
            out.write("{0:03b}".format(7) + comp + dest + jmp)
        elif p.commandType == COMMAND_TYPE.L_COMMAND.value:
            print(p.symbol())
        
        if p.current + 1 <= len(p.commands) - 1:
            out.write("\n")
    out.close()

if __name__ == "__main__":
    main()