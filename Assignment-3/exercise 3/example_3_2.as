#Initialize all Registers with numbers
ldc R0 10
ldc R1 20
ldc R2 30
ldc R3 40

#print all values
prr R0
prr R1
prr R2
prr R3

#swap R0 with R3 and R1 with R2

swp R0 R3
swp R1 R2

#print all values again

prr R0
prr R1
prr R2
prr R3

hlt
