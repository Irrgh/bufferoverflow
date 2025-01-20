// scanf
void safe_function() {
    char buffer[20];
    scanf("%19s", buffer);  // Limits input to 19 characters
}

//fgets
void safe_function() {
    char buffer[20];
    printf("Enter input: ");
    fgets(buffer, sizeof(buffer), stdin);  // Reads up to 19 characters + null terminator
    buffer[strcspn(buffer, "\n")] = '\0';  // Remove newline character if present
}
