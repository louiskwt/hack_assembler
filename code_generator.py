from typing import NewType

THREE_BIT_STR = NewType('THREE_BIT_STR', str)
SEVEN_BIT_STR = NewType('SEVEN_BIT_STR', str)

class CodeGenerator:

    def dest(self, mnemonic: str) -> THREE_BIT_STR:
        dest_lst = ["null", "M", "D", "MD", "A", "AM", "AD", "AMD"]
        if mnemonic not in dest_lst:
            raise ValueError("Invalid Code")
        dest_bits = "{0:03b}".format(dest_lst.index(mnemonic))
        assert len(dest_bits) == 3, f"Expected length 3, but got {len(dest_bits)}"
        return dest_bits

    def comp(self, mnemonic: str):
        # Comp dict for a = 0
        COMP_A0 = {
            "0": 42,
            "1": 63,
            "-1": 58,
            "D": 12,
            "A": 48,
            "!D": 13,
            "!A": 49,
            "-D": 15,
            "-A": 51,
            "D+1": 31,
            "A+1": 55,
            "D-1": 14,
            "A-1": 50,
            "D+A": 2,
            "D-A": 19,
            "A-D": 7,
            "D&A": 0,
            "D|A": 21
        }
        # comp table for a = 1
        COMP_A1 = {
            "M": 112,
            "!M": 113,
            "-M": 115,
            "M+1": 119,
            "M-1": 114,
            "D+M": 66,
            "D-M": 83,
            "M-D": 71,
            "D&M": 64,
            "D|M": 85
        }
        if mnemonic in COMP_A0:
            a0_comp_bits = "{0:07b}".format(COMP_A0[mnemonic])
            assert len(a0_comp_bits) == 7, f"Expected length 7 from output, but got {len(a0_comp_bits)}" 
            return a0_comp_bits
        elif mnemonic in COMP_A1:
            a1_comp_bits = "{0:07b}".format(COMP_A0[mnemonic])
            assert len(a1_comp_bits) == 7, f"Expected length 7 from output, but got {len(a1_comp_bits)}" 
            return a1_comp_bits
        raise ValueError("Invalid Code")

    def jump(self, mnemonic: str = "null") -> THREE_BIT_STR:
        jmp_lst = ["null", "JGT", "JEQ", "JGE", "JLT", "JNE", "JLE", "JMP"]
        if mnemonic not in jmp_lst:
            raise ValueError("Invalid Code")
        jump_bits = "{0:03b}".format(jmp_lst.index(mnemonic))
        assert len(jump_bits) == 3, f"Expected length 3, but got {len(jump_bits)}"
        return jump_bits