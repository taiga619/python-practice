#include <stdio.h>

int main(void) {
    int a[5] = {3, 1, 4, 1, 5};
    int *p = a;
    int sum = 0;
    for (int i = 0; i < 5; i++){
        sum += *p;
        p++;
    }
    printf("合計 = %d\n", sum);
    return 0;
}