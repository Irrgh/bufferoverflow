## What are we doing?

We want to overwrite a pointer which is responsible for indicating an address where the program must continue after completing current function.

So, the pointer you want to overwrite is: **the saved rip (Instruction Pointer)** stored in the stack frame (view it with _info frame_ while debugging in gdb).
This pointer is crucial because it tells the program where to return after completing the current function.


### How to use example01

To compile:
```shell
gcc -fno-stack-protector -z execstack -o example01 example01.c
```
This way we get an executable file "example01", that we can run.
#### Exercise 1
Now please execute the file and enter some text. How many characters cause any kind of error?


#### Exercise 2
Given the way the stack frame is constructed subtract 8 from the number you got and it is the size of your buffer that you can see in the source code. Run the executable in debugger.
```shel
gdb ./example01
break your_input
break doit
```
Explanation:
  First function opens example01 in GNU Project Debugger
  Next functions create breakpoints on your_input & doit functions. So when the program comes to execute those functions it stops for us so we can take a look into this program.

Now please start the program with "run" command and take the look at the stack and enter 8 'A' (ASCII code in hex for A is 41). Can you find it?
```shell
run
x/32x $rsp
continue
AAAAAAAA
x/32x $rsp
continue
```
You can also just write 'c' and submit it with enter to continue instead of writing the whole word.

#### Exercise 3
Now that you know how to create breakpoints, view stack and continue you are almost ready to complete this and hopefully the next example.

But what you need to know more is:
- How do I find the address of the instruction that I want to run?

In this example we want to run return instruction of the main function to avoid printing second message (this one ->"or... maybe not?")

To find it out run in the different tab / window another terminal and navigate to example01 directory. Run to disassemble
```shell
objdump -d example01
```
and search for retq instruction in main function. Calculate the difference between the address of <_main> and the retq instruction.

![return](./return.png)
Now please come back to the window with running debugger and type:
```shell
run
info address main
```
Copy the address and add the number you calculated before. Remember that those are hex values so use your favourite programming language or an online tool to get the result.

#### Exercise 4

Following steps do in another terminal. Do not exit the debugger so you do not have to set the breakpoints again.
Create payload by adjusting a python script in your favourite text editor (hopefully vim :-D). You just need to change the address on 5th line (print_flag_address variable) 
```shell
vim ../helper.py
```
Remember to save by clicking :wq 

Execute the script to create the payload.bin file in your current directory.
```shell
python3 ../helper.py
```
How does the payload look like? Can you explain the structure?

#### Exercise 5

Now get back to the debugger window and do:
```shell
run < payload.bin
info frame
x/32x $rsp
c
info frame
x/32x $rsp
c
```
Can you see the address that was injected?

### MOST IMPORTANT GDB COMMANDS

next - steps one line further in your program
continue - continues to the next breakpoint
x/32x $rsp - prints 32 blocks (every consisting of 8 * 16 bits written in hex)
info frame - prints information about current stack frame
break - creates a breakpoint

b <function_name> ; creates a breakpoint at an address of a function
For example:
```shell
b your_input
```

p <function_name> ; returns current address of the instruction. It usually has to be done while the program is already running, 
and you are at a breakpoint to discover the address that you want to pass to helper.py. 
For example:
```shell
p your_input
```

