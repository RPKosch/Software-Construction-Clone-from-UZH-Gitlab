ldc R0 0
ldc R1 2
prr R1
beq R0 5
# This print should not get executed
prr R1
hlt