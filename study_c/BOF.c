#include <stdio.h>

int main(){
    char food[5];
    printf("type your favorite food:");
    scanf("%s", food);
    printf("your favorite is %s\n", food);

    printf("---%s", *(&food ));
    printf("---full%s", food );
    printf("---1st%s", food[0] );
    //printf("---9th%s", food[9] );
    puts("asdas");
}