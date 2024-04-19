#Initialize
#start index
ldc R0 @array
#length of array
ldc R1 7

#Load numbers
ldc R2 1
str R2 R0
inc R0

ldc R2 2
str R2 R0
inc R0

ldc R2 3
str R2 R0
inc R0

ldc R2 4
str R2 R0
inc R0

ldc R2 5
str R2 R0
inc R0

ldc R2 6
str R2 R0
inc R0

ldc R2 7
str R2 R0

#print the array before Reverse N times
ldc R0 @array
cpy R2 R1

loop1:
prm R0
inc R0
dec R2
bne R2 @loop1

#check if length is 1 or 0 -> We do not have to change anything
beq R1 @end
dec R1
beq R1 @end
inc R1

#get front and end index of array
ldc R0 @array
add R1 R0
dec R1

loop:
ldr R2 R0
ldr R3 R1
str R3 R0
str R2 R1

#copy current front and end indexes
cpy R2 R0
cpy R3 R1

#Update Index of Array
inc R0
dec R1

#check if we front index is equal or bigger than end index
# and then terminate -> else: continue loop
sub R3 R2
#prr R3 lookup for distance between front and end index before dec and inc
beq R3 @end
dec R3
beq R3 @end
bne R3 @loop

end:
#print array
cpy R3 R1
ldc R2 @array

prm R2
inc R2

prm R2
inc R2

prm R2
inc R2

prm R2
inc R2

prm R2
inc R2

prm R2
inc R2

prm R2
inc R2

hlt
.data
array: 10












