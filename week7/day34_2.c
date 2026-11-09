#include <stdio.h>

int main(void){
    unsigned int x = 0x05;
    printf("そのまま:0x%02X\n", x);
    x |= (1 << 3);
        printf("bit3を立てる:0x%02X\n", x);
    x &= ~(1 << 0);
        printf("bit0を下げる:0x%02X\n", x);
    x ^= (1 << 2);
        printf("bit2を反転する:0x%02X\n", x);
    return 0;
}