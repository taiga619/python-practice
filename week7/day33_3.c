#include <stdio.h>

int max_of(int *arr, int n){
    int s = arr[0];
    for (int i = 0; i < n; i++){
        if (s < arr[i])
            s = arr[i];
    }
    return s;
}

int main(void){
    int a[5] = {3, 9, 2, 7, 20};
    int max = max_of(a, 5);
    printf("最大値 = %d\n", max);
}
