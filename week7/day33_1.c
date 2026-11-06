#include <stdio.h>

int main(void) {
    int a[4] = {10, 20, 30, 40};
    int *p = a;
    for (int i=0; i < 4; i++){
        printf("i=%d: 値=%d, アドレス=%p\n", i, p[i], (void )&p[i]);
    }
    return 0;
}