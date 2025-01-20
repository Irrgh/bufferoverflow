
void unsafe_function() {
    char buffer[20];
    scanf("%s", buffer);  // Warum ist das sicher?
}

// TODO: Es gibt viele andere Möglichkeiten, die ihre Vor- und Nachteile haben wie z.b
//  memcpy(), strcpy(), read(), write()
