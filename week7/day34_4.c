#include <stdio.h>

#define TX_BUSY (1<<0)
#define RX_READY (1<<1)
#define IRQ_EN (1<<3)

typedef struct{
    unsigned int ctrl;
    unsigned int status;
} UartRegs;

int main(void){
    UartRegs regs = {0x00, 0x02};
    UartRegs *uart = &regs;
    if (uart->status & TX_BUSY){
        printf("送信中\n");
    }
    else{
        printf("送信可\n");
    } 
    if (uart->status & RX_READY){
        printf("受信あり\n");
    }
    else{
        printf("受信なし\n");
    } 

    uart->ctrl |= IRQ_EN;
    printf("ctrl=0x%2X\n",uart->ctrl); 
 
    uart->status = 0x03;
    if (uart->status & TX_BUSY){
        printf("送信中\n");
    }
    else{
        printf("送信可\n");
    } 
    if (uart->status & RX_READY){
        printf("受信あり\n");
    }
    else{
        printf("受信なし\n");
    }   
}

