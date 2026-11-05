#include <stdio.h>

typedef struct {
    int hp;
    int atk;
} Unit;

void take_damage(Unit *u , int damage){
    u -> hp = u -> hp - damage;
}

int main(void){
    Unit hero = {100, 30};
    printf("ヒーローのHPは%dです\n", hero.hp);
    take_damage(&hero ,25);
    printf("ヒーローのHPは%dです\n", hero.hp);
    return 0;
}