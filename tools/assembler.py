#!/usr/bin/env python3
import sys

# Opcode mapping
OPCODES = {
    "LOAD": 0x01,
    "STORE": 0x02,
    "ADD": 0x03,
    "SUB": 0x08,           # Subtract
    "JUMP": 0x04,
    "IFNZ": 0x0A,          # Jump if Not Zero
    "HALT": 0x05,
    "PUSH": 0x06,
    "POP": 0x07,
    "DEC": 0x09,           # Decrement
    "CALL_FFI": 0xF0,
    "SYMBOL_DEFINE": 0xE0,
    "SYMBOL_APPLY": 0xE1,
    "META_REFLECT": 0xE2,
}

REGISTERS = {
    "R0": 0x00,
    "R1": 0x01,
    "R2": 0x02,
    "R3": 0x03,
}

CONSTANTS = {}

def expand_constants(token):
    """Replace constants in operands."""
    if token in CONSTANTS:
        return str(CONSTANTS[token])
    return token

def parse_operand(operand, labels, pc):
    operand = operand.strip(",")
    operand = expand_constants(operand)
    if operand.upper() in REGISTERS:
        return REGISTERS[operand.upper()]
    elif operand.startswith("0x"):
        return int(operand, 16)
    elif operand.isdigit():
        return int(operand)
    elif operand in labels:
        return labels[operand]
    else:
        raise ValueError(f"Unknown operand: {operand}")

def is_comment_or_empty(line):
    """Check if line is a comment or empty"""
    return (
        not line or
        line.startswith("//") or
        line.startswith("#") and not line.startswith("#define")
    )

def first_pass(lines):
    """Record labels and constants"""
    labels = {}
    pc = 0
    for lineno, line in enumerate(lines, 1):
        line = line.strip()
        if is_comment_or_empty(line):
            continue
        if line.startswith("#define"):
            parts = line.split()
            if len(parts) != 3:
                raise ValueError(f"Invalid constant definition at line {lineno}")
            CONSTANTS[parts[1]] = int(parts[2])
        elif line.endswith(":"):
            label = line[:-1].strip()
            if label in labels:
                raise ValueError(f"Duplicate label '{label}' at line {lineno}")
            labels[label] = pc
        else:
            parts = line.split()
            opcode = parts[0].upper()
            if opcode not in OPCODES:
                raise ValueError(f"Unknown opcode '{opcode}' at line {lineno}")
            pc += 1 + (len(parts) - 1)
    return labels

def second_pass(lines, labels):
    """Assemble instructions with resolved labels and constants"""
    program = []
    pc = 0
    for lineno, line in enumerate(lines, 1):
        line = line.strip()
        if is_comment_or_empty(line):
            continue
        if line.endswith(":"):
            continue
        parts = line.split()
        opcode = parts[0].upper()
        if opcode not in OPCODES:
            raise ValueError(f"Unknown opcode: {opcode}")
        bytecode = [OPCODES[opcode]]
        for operand in parts[1:]:
            bytecode.append(parse_operand(operand, labels, pc))
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
