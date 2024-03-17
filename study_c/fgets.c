#include <stdio.h>

int main(){
    char food[5];
    printf("type your favorite:");
    fgets(food, sizeof(food), stdin);
    printf("your favorite is %s", food);
}


