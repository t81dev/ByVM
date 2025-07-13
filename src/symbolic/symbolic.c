#include "symbolic.h"
#include <stdio.h>

static Symbol symbol_table[MAX_SYMBOLS];

void symbolic_init(void) {
    for (int i = 0; i < MAX_SYMBOLS; ++i) {
        symbol_table[i].id = 0;
        symbol_table[i].value = 0;
    }
    printf("[Symbolic] Symbolic table initialized.\n");
}

void symbol_define(uint8_t id, uint8_t value) {
    symbol_table[id].id = id;
    symbol_table[id].value = value;
    printf("[Symbolic] Defined symbol 0x%02X = %d\n", id, value);
}

void symbol_apply(uint8_t id) {
    if (symbol_table[id].id != 0) {
        printf("[Symbolic] Applied symbol 0x%02X = %d\n", id, symbol_table[id].value);
    } else {
        printf("[Symbolic] Undefined symbol 0x%02X\n", id);
    }
}

void meta_reflect(void) {
    printf("[Meta] Reflection triggered.\n");
    symbol_print_all();
}

void symbol_print_all(void) {
    printf("[Symbolic] Current Symbol Table:\n");
    for (int i = 0; i < MAX_SYMBOLS; ++i) {
        if (symbol_table[i].id != 0) {
            printf("  Symbol 0x%02X = %d\n", symbol_table[i].id, symbol_table[i].value);
        }
    }
}

void symbolic_table_dump(void) {
    printf("[Symbolic] Current Symbol Table:\n");
    for (int i = 0; i < 256; ++i) {
        if (symbol_table[i].value != 0) { // Only print nonzero entries
            printf("  Symbol 0x%02X = %d\n", i, symbol_table[i].value);
        }
    }
}
