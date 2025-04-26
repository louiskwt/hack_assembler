from parser import Parser

def main():
    print("Hack Assembler")
    p = Parser("Add.asm")
    while p.hasMoreCommand:
        p.advance()

if __name__ == "__main__":
    main()