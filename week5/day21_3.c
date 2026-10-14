#include <stdio.h>

int main(void) {
    int scores[5] = {60, 70, 80, 90, 100};
    int sum = 0;
    for (int i = 0; i <5; i++) {
        sum += scores[i];
    }
    printf("合計は %d 、平均は %d です。\n", sum, sum / 5);
    int *p = scores;
    printf("*p=%d, *(p+1)=%d, *(p+2)=%d \n", *p, *(p+1), *(p+2));
    int x = 10;
    int *q = &x;
        *q = 99;
        printf("x = %d\n", x);
    return 0;
}