#ifndef SYMBOLIC_H
#define SYMBOLIC_H

#include <stdint.h>

#define MAX_SYMBOLS 256

typedef struct {
    uint8_t id;
    uint8_t value;  // Later: support arbitrary data
} Symbol;

// Initialize the symbolic table
void symbolic_init(void);

// Define a new symbol (ID -> value)
void symbol_define(uint8_t id, uint8_t value);

// Apply a symbol (e.g., print or use its value)
void symbol_apply(uint8_t id);

// Perform meta-reflection (placeholder)
void meta_reflect(void);

// Debug: Print all symbols
void symbol_print_all(void);

#endif
