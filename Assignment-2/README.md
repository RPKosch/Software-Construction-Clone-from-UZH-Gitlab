# Assignment 2

# Supported Operations

## Additon:
Format: ["add, a ,b]

Function: Adds a and b

## Subtraction:
Format: ["subtract", a, b]

Function: Subtracts b from a

## Absolut:

Format: ["absolut", a]

Function: provides the absolut of a

## Multiplication:
Format: ["multiply", a, b]

Function: Multiplys a with b

## Division:
Format: ["divide", a, b]

Function: Divides a with b

## Power:
Format: ["power", base, exponent]

Function: a<sup>b

## Set:
Format: ["set", "variable", value]

Function: Sets the variable given equals the value given

## Get:
Format: ["get", "variable"]

Function: Returns whatever the Variable holds (Int, String, Dict or Array)

## Print:
Format: ["print", xxxxx]

Function: Prints whatever datatype xxxxx is (mostly needs a ["get", variable] as xxxxx to work)

## While:
Format: 

    ["while", ["leq", ["get", "counter"], 5],
        ["seq",
            ["print", ["get", "counter"]],
            ["set", "counter", ["add", ["get", "counter"], 1]]
        ]
    ]
Function: leq (less or equal) serves as the condition (<=) as long as counter (which we defined before) fulfills this condition the "seq" in the loop is executed.

seq allows us to run multiple statements consecutive 



## Arrays:
    
### Create Array:
Format: ["array_create", size]

Function: Creates an array with length "size"

### Array Set:
Format: ["array_set", ["get", array"], index, value]

Function: Sets the value at "index" of array equals to "value"

### Array Get;
Format: Format: ["array_get", ["get", array"], index]

Function: Returns the Value at "index" in the array


## Dictionarys 

### Create Dict:
Format: ["dict_create"]

Format: Creates an empty Dictionary (you need to use "set" to safe it to a variable)

### Set Dict:
Format: ["dict_set", ["get","my_dict"], "key", value]

Function: Sets the value of "key" equals to "value" (again you need the ["get",....] part for it to function)

### Get Dict:
Format: ["dict_get", ["get", "my_dict"], "key"]

Function: Returns the value of the Dict of "key" (once more use "get")

### Merge Dict:
Format: ["merge_dict", "dict1", "dict2"]

Function: Merges dict1 and dict2 into one dict. If two keys are the same it prioritises the higher value.

### Envs_set:

Sets the enviroment to a desired function or value

### Envs_get:

provides a specified part of the environment

## OOP:

### Shape, Circle and Square:
All of them initialize the foundation of their class and Circle and Square set Shape as their parent.

### Class Methods:

#### Shape_new and Shape_density:
Shape_new creates a new shape with a name and class : Shape
Shape_density calculates the density of an object by dividing weight / area, only works for subclasses 

#### Square_new and Circle_new
Both functions create a new object of class square or circle. Both of them use shape_new to create the framework.

#### Square_area and Circle_area
Both functions calculate the area of the object. Square and circle use different calculations.

### Define new Object:
Format: ["make", "Class", "name", "value"]

Function: creates a new object of Class with the specified values and names.

### Do function with Object:
Format: ["ccall", "name", "function_name", "value"]

Function: executes the Function with the given variables.

## Functions:

The code also provides an option to create your own function with LGL

Format: ["set", "function_name", ["func", "variable/s", [desired function]]]

to call: ["call", "function_name", ["get", "some_variable"]] or ["call", "function_name", "value]


# How to run:

Python lgl_interpreter.py [filename of file you want to execute] [--trace "name of file you want to trace into"]

Python reporter.py [filename of file you traced into]


# Tracer Function:
The tracer function Traces if certain functions get used, when they get used and provides an id for them.
It traces: do_call,

Format:
_id,function_name,event,timestamp_


# Reporter Function:

The script will print a table summarizing the execution statistics for each function.

It outputs:
- Function Name: The name of the traced function.
- Number of calls: The number of times the function was called.
- Total Time (ms): The total execution time in milliseconds.
- Average Time (ms): The average execution time per call in milliseconds.


## Workflow:
1. Splitting the work
2. create a new GitLab for the project
3. reading into the topic, possibly repetition of the lecture and looking up the reading
4. regular correction together (approx. weekly)
5. discussion and mutual help in case of problems
6. fix all the stuff we did wrong in the first place

### Design choises:
1. We decided to stay loyal to the lgl_interpreter already showcased in the lecture for compatibility reasons
2. We steadily updated example-operations.gsc to steadily test if the newly implemented features work and to make sure we did not mess with the earlier implementations.
3. Same with example-class.gsc
4. In the beginning we chose to write logger in a separate file, so we do not have to change stuff in it to make it compatible.  


_Created by Ralph Kosch, Marlon Anderes and Nico Auf der Maur_