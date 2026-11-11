#include <stdio.h>
#include <stdint.h>

typedef struct {
    volatile uint32_t data;
    volatile uint32_t status;
    volatile uint32_t ctrl;
    volatile uint32_t baud;
} UartRegs;

#define STATUS_TX_BUSY  (1u << 0)
#define STATUS_RX_READY (1u << 1)
#define CTRL_TX_EN      (1u << 0)
#define CTRL_RX_EN      (1u << 1)
#define CTRL_IRQ_EN     (1u << 3)

UartRegs fake = {0x00, 0x00, CTRL_IRQ_EN, 0x00};   // ctrl は 0x08 から始まる
#define UART (&fake)

void uart_init(uint32_t baud_div) {
    UART -> baud = baud_div;
    UART -> ctrl |= CTRL_TX_EN | CTRL_RX_EN;
}

int uart_getc(void) {
    if(!(UART -> status & STATUS_RX_READY)) {
        return -1;
    }
    return (UART -> data & 0xFF);
}

int main(void){
    int r = uart_getc();
    printf("受信なし:%d\n", r);

    UART -> status = STATUS_RX_READY;
    UART -> data = 0x141;
    r = uart_getc();
    printf("受信なし:0x%X\n", r);
    return 0;
}