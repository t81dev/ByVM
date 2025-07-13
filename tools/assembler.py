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

def parse_operand(operand, labels, pc):
    operand = operand.strip(",")
    if operand.upper() in REGISTERS:
        return REGISTERS[operand.upper()]
    elif operand.startswith("0x"):  # Hex literal
        return int(operand, 16)
    elif operand.isdigit():  # Decimal literal
        return int(operand)
    elif operand in labels:  # Label
        return labels[operand]
    else:
        raise ValueError(f"Unknown operand: {operand}")

def first_pass(lines):
    """Record label positions"""
    labels = {}
    pc = 0  # Program counter
    for lineno, line in enumerate(lines, 1):
        line = line.strip()
        if not line or line.startswith("//") or line.startswith("#"):
            continue  # Skip comments and empty lines
        if line.endswith(":"):
            label = line[:-1].strip()
            if label in labels:
                raise ValueError(f"Duplicate label '{label}' at line {lineno}")
            labels[label] = pc
        else:
            parts = line.split()
            opcode = parts[0].upper()
            if opcode not in OPCODES:
                raise ValueError(f"Unknown opcode '{opcode}' at line {lineno}")
            pc += 1 + (len(parts) - 1)  # opcode + operands
    return labels

def second_pass(lines, labels):
    """Assemble instructions with resolved labels"""
    program = []
    pc = 0
    for lineno, line in enumerate(lines, 1):
        line = line.strip()
        if not line or line.startswith("//") or line.startswith("#"):
            continue
        if line.endswith(":"):
            continue  # Label, already processed
        parts = line.split()
        opcode = parts[0].upper()
        bytecode = [OPCODES[opcode]]
        for operand in parts[1:]:
            try:
                bytecode.append(parse_operand(operand, labels, pc))
            except Exception as e:
                raise ValueError(f"Line {lineno}: {e}")
        program.extend(bytecode)
        pc += len(bytecode)
    return program

def assemble_file(input_path, output_path):
    with open(input_path, "r") as f:
        lines = f.readlines()

    try:
        labels = first_pass(lines)
        program = second_pass(lines, labels)
    except Exception as e:
        print(f"[Assembler Error] {e}")
        sys.exit(1)

    with open(output_path, "wb") as out:
        out.write(bytes(program))

    print(f"[Assembler] Assembled {len(program)} bytes to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: assembler.py <input.by> <output.bin>")
        sys.exit(1)

    assemble_file(sys.argv[1], sys.argv[2])
