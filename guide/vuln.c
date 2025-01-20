#include<stdio.h>
#include<string.h>

char* gets(char* buffer);  // Declare gets() manually

void vulnerable_function() {
    char buffer[8];    // Fixed-size buffer

    printf("Enter some text: ");
    gets(buffer);  // Unsafe: no bounds checking
    printf("You entered: %s\n", buffer);
}

int main() {
    vulnerable_function();
    return 0;
}

