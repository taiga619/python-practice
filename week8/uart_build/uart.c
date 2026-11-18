#include "uart.h"

void uart_init(UartRegs *u){
    u -> ctrl |= CTRL_EN;
}

void uart_putc(UartRegs *u, char c){
    while ((u -> status & TX_READY) == 0){}
        u -> data = c;
}