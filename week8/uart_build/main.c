#include <stdio.h>
#include "uart.h"

int main(void){

UartRegs fake = {0, TX_READY, 0};

uart_init(&fake);
uart_putc(&fake, 'A');

printf("data=%c ctrl=%u\n", (char)fake.data, (unsigned)fake.ctrl);

return 0;
}