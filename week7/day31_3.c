#include <stdio.h>
typedef struct {
    int amount;
    char title[20];
} Record;

int main(void) {
    Record records[3];
    records[0].amount = 800;
    records[1].amount = 300;
    records[2].amount = 1200;
    int sum = 0;
    for (int i = 0; i < 3; i++) {
        sum += records[i].amount;
    }
    printf("合計: %d\n", sum);
    return 0;
}