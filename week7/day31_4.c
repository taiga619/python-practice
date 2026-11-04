#include <stdio.h>
typedef struct {
    int hp;
    int atk;
} Unit;

int main(void) {
    Unit a;
    Unit b;
    a.hp = 100;
    a.atk = 30;
    b.hp = a.hp - 40;
    b.atk = a.atk / 2;
    printf("b.hp: %d, b.atk: %d\n", b.hp, b.atk);
    return 0;
};