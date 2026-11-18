#ifndef UART_H
#define UART_H

#include <stdint.h>

typedef struct {
    volatile uint32_t data;
    volatile uint32_t status;
    volatile uint32_t ctrl;
} UartRegs;

#define CTRL_EN (1u << 0)
#define TX_READY (1u << 0)

void uart_init(UartRegs *u);
void uart_putc(UartRegs *u, char c);

#endif