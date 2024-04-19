#Initialize all Registers with numbers
ldc R0 0
ldc R1 10

#print values
prr R0
prr R1

#check basic functionality - Both should be 1 and 9
inc R0
dec R1

prr R0
prr R1

ldc R2 0
ldc R3 20

prr R2
prr R3

loop:
inc R2
dec R3
bne R3 @loop

prr R2
prr R3

hlt

