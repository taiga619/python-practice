#include <stdio.h>
typedef struct {
    int amount;
    char title[20];
} Record;

int main(void) {
    Record r;
    r.amount = 1200;
    r.title[0] = 'a';
    r.title[1] = 'b';
    r.title[2] = '\0';
    printf("title: %s, amount: %d\n", r.title, r.amount);
    return 0;
}