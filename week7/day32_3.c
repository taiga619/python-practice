#include <stdio.h>
void double_it(int *n) {
    *n = *n * 2;
}

int main(void){
    int a= 7;
    printf("前aの値:%d\n", a);
    double_it(&a);
    printf("後aの値:%d\n", a);
    return 0;
}