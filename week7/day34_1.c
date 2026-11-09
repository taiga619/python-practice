#include <stdio.h>

int main(void){
    int a = 0x0C;
    int b = 0x0A;
    printf("a&b=0x%02X, a|b=0x%02X, a^b=0x%02X, ~a=0x%02X, a<<2=0x%02X, a>>2=0x%02X\n", a&b, a|b, a^b, ~a&(0xFF), a<<2, a>>2);
}