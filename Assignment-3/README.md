# Assignment 3



## Exercise 1

### Assembler & Virtual Machine Test Suite

This test suite evaluates the functionality and correctness of a custom-made assembler and virtual machine using Python. The suite consists of individual test cases designed to validate different assembler and virtual machine functionalities.

The following tests were implemented for Exercise 1 Task A, B and C
### Assembler Tests
* test_insert_values: Tests the insertion of values using the assembler and validates that the 	written script transforms correctly into assembly language to perform this operation.
* test_copy_register: Validates the functionality of copying registers within the assembler and ensures that the script accurately translates into assembly code for register copying.
* test_sub: Tests subtraction operations within the assembler and confirms that the written script correctly transforms into assembly language instructions for subtraction.
* test_add: Validates addition operations in the assembler and ensures that the script accurately transforms into assembly code for addition.
* test_print_memory: Ensures that saving registers into memory and printing operations are transformed correctly into assembly language.
* test_load_register: Tests loading registers in the assembler and confirms that the script accurately transforms into assembly language instructions for loading registers.
* test_branch_equal: Validates branching for equality with 0 in the assembler and ensures that the script correctly translates into assembly code for branching based on equality.
* test_branch_not_equal: Tests branching for inequality with 0 in the assembler and confirms that the script accurately transforms into assembly language instructions for branching based on inequality.
* test_out_of_memory: Checks for handling out-of-memory errors with an array that is too big and confirms that the script gives back its own Error.
* test_instructions_not_found_as: Validates handling of missing instructions in the assembler to give back an own Error.

### Virtual Machine Tests
* test_insert_values_vm: Validates inserting values using the virtual machine.
* test_copy_register_vm: Tests copying registers within the virtual machine.
* test_sub_vm: Validates subtraction operations within the virtual machine.
* test_add_vm: Tests addition operations in the virtual machine.
* test_print_memory_vm: Ensures the correct functionality that the correct assembly code saves Registers into the memory and prints the values of those memory locations.
* test_load_register_vm: Tests loading registers in the virtual machine.
* test_branch_equal_vm: Validates branching for equality with 0 in the virtual machine.
* test_branch_not_equal_vm: Tests branching for inequality with 0 in the virtual machine.
* test_instructions_not_found_vm: Validates handling of missing instructions in the virtual machine.


* B(i) assume that the Assembler is correct (how much more complicated would things be without this assumption?);  
* It would be much harder because we cannot be sure if the error occurs from vm.py or from the assembler. If we cannot be sure that it works properly we have to assembly our script always by ourselves and even this would probably result in some errors because we will also make slip-ups from time to time. 

### Running the Tests:
We run the test by typing this command in the directory of exercise 1:

```bash
pytest
```

It will automatically check all functions starting with 'test_' by executing them with the corresponding system (either the Assembler or the Virtual Machine) and subsequently comparing the output against our own solution.

### Important Note: 
I've implemented all 11 operations specified in the architecture.py file. However, I combined a few of them into single tests for practicality. Firstly, I paired the 'idc' and 'hlt' operations with most tests as they are fundamental for inputting values and halting the program. The correct functionality of these two basic operations is crucial for the success of all other tests. Additionally, I merged the 'str' and 'prm' operations in the 'print_memory' test. 'Str' loads a Register into memory, while 'prm' prints the values of a memory slot, making it sensible to test them together.

Moreover, I've included the 'instruction_not_found' test for both the assembler and the virtual machine. Although strictly it might only be necessary for the virtual machine, as the error could occur there, I added it to the assembler tests as well. This validates that both systems would provide the correct error response in such a scenario.

### The calculated coverage using: 
```bash
pytest --cov
```
is 89%. We need to consider that pytest is also calculating arrays.py which we did not need to test.
With that in mind the real coverage is probably a bit higher.


## Exercise 2

### Disassembler class:

The Disassembler class hosts the following Methodes

### disassemble(self, lines) method:
-It takes a list of machine code lines as input. These are generated by using .readlines() on the input File.
-Calls _get_lines to simplify string.
-Calls _get_instructions to decode lines into three ints (op, operand 1, operand 2).
-Calls _get_assembly to generate the wanted assembly code.
-Returns a list of disassembled assembly instructions.

### _get_lines(self, lines) method:
-Strips whitespace from each line.
-Removes empty lines.
-Returns a cleaned list of lines.

### _get_instructions(self, lines) method:
-Decodes each line into three integers (op, operand 1, operand 2).
-Decodes them using _decode.
-Uses _get_instructions_from_OPS to get instruction details based on the OPS code.
-Constructs a list of instructions with their names, operands, and format types.
-Returns a list of instructions.

### _decode(self, line) method:
-Decodes the string representation of a line into three integers (OP code, operand 1, operand 2 using (int(line[4:6],16),int(line[2:4],16),int(line[0:2],16))
-Returns a list of these three integers.

### _get_instructions_from_OPS(self, wanted) method:
-Searches for an instruction in the OPS module based on the provided OP code.
-Returns a dictionary containing the instruction name and format type.

### _get_assembly(self, instructions) method:
-Converts the list of instructions into a list of disassembled assembly instructions.
-Handles different operand types (registers, labels) and constructs the assembly code accordingly.
-Returns a list of disassembled assembly instructions.

### main(disassembler) function:
-Takes a Disassembler class instance as an argument.
-Validates the command-line arguments.
-Reads input from a file or standard input.
-Calls the disassemble method of the Disassembler instance to obtain the disassembled program.
-Writes the disassembled program to an output file or standard output.

You use the file with the following command. You need to swap inputfile/outputfile with the real filename.
```bash
python disassembler.py inputfile.mx outputfile.as
```

## Exercise 3

### 3.1 inc and dec operations
To introduce new operations to our assembler and virtual machine, we begin by updating the 'architecture.py' file. Within this file, we assign a name to the new operation and allocate the next available hex number that hasn't been used yet. For operations like 'inc' and 'dec,' we adopt the format prefix 'r-' as a convention. This notation is chosen because incrementing or decrementing a value requires access to a single register, where we consistently add or subtract 1.

Subsequently, we modify the 'run' function within the 'vm.py' file to define the behavior of these new operations. To do so, we utilize the 'self.register' attribute, incrementing it by 1 for the 'inc' operation and decrementing it by 1 for the 'dec' operation.

We can show that those two operations work with the following command in the terminal of exercise 3:
```bash
python assembler.py example_3_1.as output_3_1.mx 
```
```bash
python vm.py output_3_1.mx - 
```

### 3.2 swp operations
For this exercise, we begin by updating the architecture file to introduce a new operation named 'swp.' To facilitate the swapping of two registers, we designate the format prefix as 'rr'.

Next, we extend the functionality of this operation within the 'run' function in the 'vm.py' file. To execute a swap of elements between registers without impacting other values, we employ a temporary variable. The first register's content is stored in this temporary variable, allowing it to be overwritten by the content of the second register. Subsequently, the second register receives the initial value stored in the temporary variable. Accessing the registers at their respective spots is achieved using the code snippet 'self.reg.'

We can demonstrate the functionality of these two operations using the following command in the terminal of exercise 3:
```
python assembler.py example_3_2.as output_3_2.mx 
```
```bash
python vm.py output_3_2.mx - 
```

### 3.3 Reverse Array
In this exercise, I'll explain the code I've written to reverse an array of length N. To simplify the process, I've broken it down into these instructions:
### Initialize:
Set the starting index and define the array length, which in this case is 7. Access the start index of the array via '@array', and both values are stored in the first two registers.

### Load Numbers into Array:
Next, load N numbers into the memory, which was previously reserved at the bottom of our .as file during array initialization. To insert the values, we increment the array index, which points to the next available space in memory.

### Print Array before Reversal:
Display the array content before performing the reversal operation. Begin at the array's start index, printing each value while incrementing the array index.

### Check Array Length:
Verify if the array length is 1 or 0. This check is crucial because if the array has a length of 0 or 1, the array and the reversed array are the same. To prevent errors, we handle these cases and proceed to the end if no modification is needed.

### Reverse the Array:
Reverse the array by swapping elements between the front and end indexes. To achieve this, set the array length variable to the end index of the array. Create copies for both indexes and store them in Register 2 (copy of 0) and 3 (copy of 1). Load the third register into the memory at the index of Register 0, and load the second register's value into the memory at the location of Register 1. Check if the distance between the current first and last index is 0 or 1. If so, exit the loop; otherwise, decrement the current last index and increment the current first index.

### Print Reversed Array:
Finally, display the reversed array as done previously.

### Run
To demonstrate the reversal of the array, execute the following command in the terminal of exercise 3:
```bash
python arrays.py example_3_3.as output_3_3.mx 
```
```bash
python vm.py output_3_3.mx -
```

## Debugger
### The debugger consists of 5 files:
- Architecture.py defines the standard virtual machine foundations like what operations it can do and what states it has.
- vm_base.py defines the class VirtualMachine. There are instructions on what to do with input and what happens if you run the programm
- vm_step.py inherits VirtualMachine from vm_base.py and builds upon it by allowing the user to use the step command and introduing basic commands but not yet defining them
- vm_extend.py inherits from vm_step.py and extends its functionality once again by now defining the before mentioned commands and allowing the user to interact with the debugger
- vm_break.py is the final version and inherits from vm_extend.py. The debugger is now extended by breakpoints and watchpoints which allow the user to run the programm and only stop at certain points.

To run the debugger you need to use the vm_break.py file because it inherits from all opther files and extends the functionality.
You run it by typing in ther terminal:
```bash
python vm_break.py inputfile.mx
```

### All available commands (you don't have to type the full commands in the terminal, but only excerpts of the words):

- ### run
The whole programm runs until it either encounters a breakpoint, watchpoint or is finished

- ### step
The next instruction for the programm gets executed

- ### dis
Shows the next intruction for your programm in the terminal

- ### ip
Shows your current address in the terminal

- ### memory
First asks for you to give it one or two addresses of which you want the memory.
If you give it two numbers seperated by a space, it prints all memories between these two addresses in ther terminal, else it prints only one memory

- ### quit
Stops the programm at the current location and prints all current registers, memories and the ip.

- ### break
Asks for you to give it an address, if you just press enter, it takes the current address.
Afterwards it sets a breakpoint at the given address

- ### clear
Asks for you to give it an address, if you just press enter, it takes the current address.
Deletes the breakpoint at the given address

- ### watchpoint
Asks for you to give it an address, if you just press enter, it takes the current address.
Sets a watchpoint at that address.
A watchpoint ends the programm at the given address and prints the current statistics.


## Changes made in the debugger by us:
### _do_memory(self, addr)
first asks for user input to determine which memory should be shown
then checks if multiple or one inputs are given
then writes every memory in the terminal

### interact(self, addr)
the given input is saved in a variable
it checks if the variable is in self.handlers, but only from the first character to the amount of given characters that are supplied are taken in consideration to prevent taken any random character from a word
if the variable is in self.handlers, the given command is then executed

### _do_add_breakpoint(self, addr)
the method is supplied an address
first the user gets asked at which address they want to set a breakpoint
if the user doesn't enter one, the supplied address from the start is used
the address of the breakpoint gets saved in a dictionary and the ram address gets replaced by the code of the vm for break

### _do_add_breakpoint(self, addr)
the method is supplied an address
first the user gets asked at which address they want to clear the breakpoint
if the user doesn't enter one, the supplied address from the start is used
the address of the breakpoint gets deleted from the dictionary and the ram address gets restored

### do_watchpoint(self, addr)
first the user gets asked at which address they want to clear the breakpoint
if the user doesn't enter one, the supplied address from the start is used
the address is saved in a list

### run(self)
if self.ip is in the list for watchpoints, the state of the vm is set to Finished


## Workflow:
1. Splitting the work
2. create a new GitLab for the project
3. reading into the topic, possibly repetition of the lecture and looking up the reading
4. regular correction together (approx. weekly)
5. discussion and mutual help in case of problems
6. fix all the stuff we did wrong in the first place

## Running the main VM
All exercises that use a vm (except debugger and pytest) can be run from outside the dedicated folder, but then the path to the folder has to be supplied.
For example for exercise 3.3:
```bash
python ..\vm\arrays.py '..\exercise 3\example_3_3.as' '..\exercise 3\example_3_3.mx'
```
But every exercise also has its private vm which can be used without the path in front.


_Created by Ralph Kosch, Marlon Anderes and Nico Auf der Maur_