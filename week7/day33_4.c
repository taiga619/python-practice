#include <stdio.h>

void add_each(int *arr, int n, int d) {
    for (int i = 0; i < n; i++){
        arr[i] += d;
    }
}

int main(void){
    int a[4] = {1, 2, 3, 4};
    printf("前: ");
    for (int i=0; i < 4; i++){
        printf("%d ", a[i]);
    }
    printf("\n");

    add_each(a, 4, 20);
    printf("後: ");
    for (int i=0; i < 4; i++){
        printf("%d ", a[i]);
    }
    printf("\n");
}