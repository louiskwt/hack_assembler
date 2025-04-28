import argparse
from parser import Parser, COMMAND_TYPE
from code_generator import CodeGenerator
from symbol_table import SymbolTable

def main():
    print("-------------Hack Assembler-------------")
    arg_parser = argparse.ArgumentParser(description="handle input assembly file")
    arg_parser.add_argument("-f", dest="file", type=argparse.FileType('r'))
    args = arg_parser.parse_args()
    file_name = args.file.name
    p = Parser(file_name)
    code = CodeGenerator()
    symbols = SymbolTable()
    # first pass
    while p.hasMoreCommand:
        p.advance()
        if p.currentCommandType == COMMAND_TYPE.A_COMMAND.value:
            symbol = p.symbol()
            if  not symbols.contains(symbol):
                address = int(symbol) if symbol.isnumeric() else None
                symbols.addEntry(symbol, address)
        if p.currentCommandType == COMMAND_TYPE.L_COMMAND.value:
            symbol = p.symbol()
            if not symbols.contains(symbol):
                symbols.addEntry(symbol, p.current)
    
    p.restart()
    out = open(file_name.split(".")[0] + ".hack", "+w")
    print(symbols.table)

    # Second pass
    while p.hasMoreCommand:
        p.advance()
        if p.currentCommandType == COMMAND_TYPE.A_COMMAND.value:
            symbol = p.symbol()
            print(symbol)
            out.write("{0:016b}".format(symbols.getAddress(symbol)))
        elif p.currentCommandType == COMMAND_TYPE.C_COMMAND.value:
            dest_code = p.dest()
            dest = code.dest(dest_code if dest_code else "null")  
            comp = code.comp(p.comp())
            jmp_code = p.jump() 
            jmp = code.jump(jmp_code if jmp_code else "null")
            out.write("{0:03b}".format(7) + comp + dest + jmp)
        elif p.commandType == COMMAND_TYPE.L_COMMAND.value:
            symbol = p.symbol() 
            out.write("{0:016b}".format(symbols.getAddress(symbol)))

        if p.current + 1 <= len(p.commands) - 1:
            out.write("\n")
    out.close()

if __name__ == "__main__":
    main()