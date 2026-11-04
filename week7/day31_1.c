#include <stdio.h>
struct Record {
    int amount;
    char title[20];
};

int main(void) {
    struct Record r;
    r.amount = 800;
    r.title[0] = 'A';
    r.title[1] = '\0';
    printf("title: %s, amount: %d\n", r.title, r.amount);
    return 0;
}