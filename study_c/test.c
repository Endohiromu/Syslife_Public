#include <stdio.h>

int main(){
    char name[40];
    printf("type your name\n");
    scanf("%39s", name);
    printf("type your %s", name);

    int age;
    printf("type your age\n");
    scanf("%i", &age);
    printf("ypu are %i years old", age);
}