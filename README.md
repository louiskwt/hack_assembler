# An Assembler For the Hack Hardware Platform

This is an assembler writen to translate assembly language into hack machine code. It's implemented using Python and this is based on the famous [Nand2Tetris Course](https://www.nand2tetris.org/)

## How it works
Symbol Table: Tracks labels/variables (e.g., LOOP, counter).

Parser:
    - A-instruction: @value → binary 0value (14-bit address).
    - C-instruction: dest=comp;jump → binary 111accccccdddjjj.

Machine Code Generator: Converts assembly to 16-bit binary executable for C-instructions