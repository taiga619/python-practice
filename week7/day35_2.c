#include <stdio.h>
#include <stdint.h>

void set_bits(volatile uint32_t *reg, uint32_t mask){
    *reg |= mask;
}

void clear_bits(volatile uint32_t *reg, uint32_t mask){
    *reg &= ~mask;
}

int main(void){
    volatile uint32_t ctrl = 0x05;
    printf("ctrl = 0x%02X\n", ctrl);
    set_bits(&ctrl, 1 << 3);
    printf("ctrl = 0x%02X\n", ctrl);
    clear_bits(&ctrl, 1 << 0);
    printf("ctrl = 0x%02X\n", ctrl);
    set_bits(&ctrl, (1 << 1) | (1 << 4));
    printf("ctrl = 0x%02X\n", ctrl);
}

