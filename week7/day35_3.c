#include <stdio.h>
#include <stdint.h>

#define TX_BUSY (1 << 0)

typedef struct {
    volatile uint32_t data;
    volatile uint32_t status;
} UartRegs;

UartRegs fake = {0x00, TX_BUSY};
#define UART (&fake)

void uart_putc(char c) {
    int polls = 0;
    while (UART -> status & TX_BUSY) {
        if (polls < 3){
            ++polls;
        }
        else {
            UART -> status &= ~TX_BUSY;
        }
    }
    UART -> data = c;
    printf("待った回数=%d, data=0x%02X\n", polls, UART -> data);
}

int main(void) {
    uart_putc('A');
    return 0;
}