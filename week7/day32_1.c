#include <stdio.h>

int main(void){
    int x = 10;
    int *p = &x;
    printf("xの値:%d, xのアドレス:%p, *pの値:%d\n", x, (void *)&x, *p);
    return 0;
}