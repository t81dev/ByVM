#include "symbolic.h"
#include <stdio.h>

static Symbol symbol_table[MAX_SYMBOLS];

void symbolic_init(void) {
    for (int i = 0; i < MAX_SYMBOLS; ++i) {
        symbol_table[i].id = 0;
        symbol_table[i].value = 0;
    }
}

void symbol_define(uint8_t id, uint8_t value) {
    symbol_table[id].id = id;
    symbol_table[id].value = value;
    printf("[Symbolic] Defined symbol 0x%02X = %d\n", id, value);
}

void symbol_apply(uint8_t id) {
    printf("[Symbolic] Applied symbol 0x%02X = %d\n", id, symbol_table[id].value);
}

void meta_reflect(void) {
    printf("[Meta] Reflection not yet implemented.\n");
}
