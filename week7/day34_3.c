#include <stdio.h>

int get_bit(unsigned int x, int n){
    return (x >> n) & 1;
}


int main(void){
    unsigned int x = 0x2D;
    for (int n = 0; n < 8; n++){
        printf("bit%d: 0x%2X\n", n, get_bit(x, n));
    }
    return 0;
}