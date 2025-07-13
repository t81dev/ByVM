#ifndef SYMBOLIC_H
#define SYMBOLIC_H

#include <stdint.h>

#define MAX_SYMBOLS 256

typedef struct {
    uint8_t id;
    uint8_t value;  // In future: make this more complex (struct or pointer)
} Symbol;

void symbolic_init(void);
void symbol_define(uint8_t id, uint8_t value);
void symbol_apply(uint8_t id);
void meta_reflect(void);

#endif
