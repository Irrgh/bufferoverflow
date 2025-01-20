#ifndef example1
#define example1
#include <stdio.h>

char* gets(char* buffer);  // Declare gets() manually
void your_input(char* buffer) {
    printf("You entered: %s\n", buffer);
}

void doit(void) {
    char buf[8];

    gets(buf);
    your_input(buf);
}

int main(void) {
    printf("So... The End... \n");
    doit();
    printf("or... maybe not?\n");

    return 0;
}
#endif
