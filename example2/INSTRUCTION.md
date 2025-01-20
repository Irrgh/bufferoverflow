### How to use example02

In this example you are supposed to use gdb (debugger for C programs) to capture the flag. It is not easy. Use cheatsheets from example1 & ask us!

In this example you have an already compiled file. You know that input is insecure and prone to buffer overflow.

Steps to forgo:
1. Find which size is the buffer (use _info frame_ and compare Locals at 0x... and Previous frame's sp is 0x... Difference between those two is the size of the array).
![size](./size.png)
2. Define how much space after filling the array you have to overflow before injecting the address of desired instruction.
3. Decompile the executable file with objdump -d example2 and search for the print_flag function. Can you guess from the name and assembly code what it does?
4. Run the executable file in gdb and find the address of the function (p print_flag)
5. Adjust python helper script
6. Run the program with the binary payload.

Did you manage to run this hidden function?
