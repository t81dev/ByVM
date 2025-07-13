#!/usr/bin/env python3
import sys

# Opcode mapping
OPCODES = {
    "LOAD": 0x01,
    "STORE": 0x02,
    "ADD": 0x03,
    "JUMP": 0x04,
    "HALT": 0x05,
    "PUSH": 0x06,
    "POP": 0x07,
    "CALL_FFI": 0xF0,
    "SYMBOL_DEFINE": 0xE0,
    "SYMBOL_APPLY": 0xE1,
    "META_REFLECT": 0xE2,
}

# Register mapping
REGISTERS = {
    "R0": 0x00,
    "R1": 0x01,
    "R2": 0x02,
    "R3": 0x03,
}

def assemble_line(line):
    line = line.strip()
    if not line or line.startswith("//") or line.startswith("#"):
        return []  # Skip comments and empty lines

    parts = line.split()
    opcode = parts[0].upper()
    if opcode not in OPCODES:
        raise ValueError(f"Unknown opcode: {opcode}")

    bytecode = [OPCODES[opcode]]

    # Handle operands
    for operand in parts[1:]:
        operand = operand.strip(",")
        if operand.upper() in REGISTERS:
            bytecode.append(REGISTERS[operand.upper()])
        elif operand.startswith("0x"):  # Hex literal
            bytecode.append(int(operand, 16))
        elif operand.isdigit():  # Decimal literal
            bytecode.append(int(operand))
        else:
            raise ValueError(f"Unknown operand: {operand}")

    return bytecode

def assemble_file(input_path, output_path):
    program = []
    with open(input_path, "r") as f:
        for lineno, line in enumerate(f, 1):
            try:
                program.extend(assemble_line(line))
            except Exception as e:
                print(f"Error on line {lineno}: {e}")
                sys.exit(1)

    with open(output_path, "wb") as out:
        out.write(bytes(program))

    print(f"[Assembler] Assembled {len(program)} bytes to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: assembler.py <input.by> <output.bin>")
        sys.exit(1)

    assemble_file(sys.argv[1], sys.argv[2])
