#include <stdio.h>

int main(void){
    int x = 10;
    int *p = &x;
    printf("前xの値:%d\n", x);
    *p = 99;
    printf("後xの値:%d\n", x);
    return 0;
}