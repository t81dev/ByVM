#ifndef SYMBOLIC_H
#define SYMBOLIC_H

#include <stdint.h>

#define MAX_SYMBOLS 256

typedef struct {
    uint8_t id;
    uint8_t value;  // Later: extend to arbitrary data
} Symbol;

// Initialize the symbolic subsystem
void symbolic_init(void);

// Define a new symbol
void symbol_define(uint8_t id, uint8_t value);

// Apply a symbol
void symbol_apply(uint8_t id);

// Print all symbols (debugging)
void symbol_print_all(void);

// Reflective meta-op
void meta_reflect(void);

#endif
