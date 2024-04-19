import json
import argparse
import math
import datetime
import random

all_id = {}  # All ID's will be saved in this global dictionary
logger_file = None  # Global file for logger and for checking if we want to log


# Function to generate a unique ID
def generate_id():
    while True:
        new_id = random.randint(1, 1000000)
        if new_id not in all_id.keys():
            all_id[new_id] = True
            return new_id


# Outer function to import additional data, in this case, the logger_file
def trace_function(function):
    # Inner function to wrap around the original function
    def _inner(*args, **kwargs):
        # Check if logger_file is provided
        if logger_file:
            # Check if all_id is empty and initialize the log file if necessary
            if all_id == {}:
                with open(logger_file, "a") as file:
                    file.write(f"id,function_name,event,timestamp\n")
                    file.flush()

            with open(logger_file, "a") as file:
                # Determine the function name
                if function.__name__ == "do_call":
                    function_name = args[1][0]
                else:
                    function_name = function.__name__

                # Log the start event
                status = 'start'
                current_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
                unique_id = generate_id()

                file.write(f"{unique_id},{function_name},{status},{current_time}\n")
                file.flush()

                # Execute the original function
                output = function(*args, **kwargs)

                # Log the stop event
                status = 'stop'
                current_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')

                file.write(f"{unique_id},{function_name},{status},{current_time}\n")
                file.flush()

                return output
        else:
            # If logger_file is not provided, simply execute the original function
            output = function(*args, **kwargs)
            return output

    return _inner


def do_subtract(envs,args):
    assert len(args) == 2
    a = do(envs,args[0])
    b = do(envs,args[1])
    return a - b


def do_absolute(envs,args):
    assert len(args) == 1
    value = do(envs,args[0])
    return abs(value)

#creates costum function
def do_func(envs, args):
    assert len(args) == 2
    var = args[0]
    rest = args[1]
    return ["func", var, rest]


def do_multiplication(envs, args):
    assert len(args) == 2
    a = do(envs, args[0])
    b = do(envs, args[1])
    return a * b



def do_division(envs, args):
    assert len(args) == 2
    a = do(envs, args[0])
    b = do(envs, args[1])
    return a / b



def do_power(envs, args):
    assert len(args) == 2
    base = do(envs, args[0])
    exponent = do(envs, args[1])
    return base ** exponent



def do_print(envs, args):
    assert len(args) == 1
    value = do(envs, args[0])
    print(value)
    return value


#determines if value is less or equal to the given condition
def do_leq(envs, args):
    assert len(args) == 2
    a = do(envs, args[0])
    b = do(envs, args[1])
    return a <= b

#makes sure that every command is run
def do_seq(envs, args):
    assert len(args) > 0
    for item in args:
        result = do(envs, item)
    return result

#gets part of the environment
def envs_get(envs, name):
    assert isinstance(name, str)
    for x in reversed(envs):
        if name in x:
            return x[name]
    assert False, f"Unknown variable name {name}"

#sets part of the environment
def envs_set(envs, name, value):
    assert isinstance(name, str)
    envs[-1][name] = value



def do_add(envs, args):
    assert len(args) == 2
    a = do(envs, args[0])
    b = do(envs, args[1])
    return a + b

#sets a variabel to a desired value
def do_set(envs, args):
    assert len(args) == 2
    assert isinstance(args[0], str)
    name = args[0]
    value = do(envs, args[1])
    envs_set(envs, name, value)
    return value

#used to calll the costum functions
@trace_function
def do_call(envs, args):
    assert len(args) >= 1
    name = args[0]
    arguments = args[1:]
    # eager evaluation
    values = [do(envs, arg) for arg in arguments]

    func = envs_get(envs, name)
    assert isinstance(func, list)
    assert func[0] == "func"
    func_var = func[1]
    assert len(func_var) == len(values)

    local_frame = dict(zip(func_var, values))
    envs.append(local_frame)
    body = func[2]
    result = do(envs, body)
    envs.pop()

    return result


def do_while(envs, args):
    assert len(args) == 2
    condition = args[0]
    body = args[1]
    result = None
    while do(envs, condition):  # Evaluate the condition
        result = do(envs, body)  # Execute the body
    return result

#gets a value from a variable given
def do_get(envs, args):
    assert len(args) == 1
    return envs_get(envs, args[0])


def do_array_create(envs, args):
    assert len(args) == 1
    size = do(envs, args[0])
    return [None] * size


def do_array_get(envs, args):
    assert len(args) == 2
    array = do(envs, args[0])
    index = do(envs, args[1])
    assert isinstance(array, list), "Expected an array"
    assert 0 <= index < len(array), "Index out of range"
    return array[index]


def do_array_set(envs, args):
    assert len(args) == 3
    array = do(envs, args[0])
    index = do(envs, args[1])
    new_value = do(envs, args[2])
    assert isinstance(array, list), "Expected an array"
    assert 0 <= index < len(array), "Index out of range"
    array[index] = new_value
    return None


def do_dict_create(envs, args):
    return {}  # Create a new dictionary


def do_dict_get(envs, args):
    assert len(args) == 2
    dictionary = do(envs, args[0])
    key = do(envs, args[1])
    assert isinstance(dictionary, dict), "Expected a dictionary"
    return dictionary.get(key, None)  # Get the value of a key or None if not found


def do_dict_set(envs, args):
    assert len(args) == 3
    dictionary = do(envs, args[0])
    key = do(envs, args[1])
    new_value = do(envs, args[2])
    assert isinstance(dictionary, dict), "Expected a dictionary"
    dictionary[key] = new_value
    return None  # Return None to indicate successful update


def do_dict_merge(envs, args):
    assert len(args) == 2
    dict1 = do(envs, args[0])
    dict2 = do(envs, args[1])
    assert isinstance(dict1, dict) and isinstance(dict2, dict), "Expected dictionaries"
    return {**dict1, **dict2}


# Instantiate the shape functions
@trace_function
def do_shape_new(name):
    return {"name": name,
            "_class": Shape}


@trace_function
def do_shape_density(thing, weight):
    return float(weight)/ do_ccall(thing, "area")


# Instantiate Square functions
@trace_function
def do_square_new(name, side):
    return do_make(Shape, name) | {"side": float(side),
                                   "_class": Square}


@trace_function
def do_square_area(thing):
    return float(thing["side"]) ** 2


# Instantiate circle functions
@trace_function
def do_circle_new(name, radius):
    return do_make(Shape, name) | {"radius": float(radius),
                                   "_class": Circle}

@trace_function
def do_circle_area(thing):
    return float(math.pi) * float(thing["radius"]) ** 2


#Used for making new objects
def do_make(cls, *args):
    if args[0][0] == "Square":
        return Square["_new"](*args[0][1:])
    elif args[0][0] == "Circle":
        return Circle["_new"](*args[0][1:])
    elif args[0][0] == "Shape":
        return Shape["_new"](*args[0][1:])

    return cls["_new"](*args)

#Used for calling methods
def do_ccall(thing, method_name):
    if isinstance(thing, list):
        thing = thing[-1]
    if "Shape" in thing:
        thing = thing[method_name[0]]
    method = do_find(thing["_class"], method_name)
    if not isinstance(method_name, list):
        return method(thing)
    return method(thing, method_name[2])

# find the correct method even in parents
def do_find(cls, method_name):
    if isinstance(method_name, list):
        method_name = method_name[1]
    while cls is not None:
        if method_name in cls:
            return cls[method_name]
        cls = cls["_parent"]
    raise NotImplementedError("method_name")

def do(envs, expr):
    if isinstance(expr, int):
        return expr
    if isinstance(expr, str):
        return expr
    assert isinstance(expr, list)
    assert expr[0] in OPERATIONS, f"Unknown operation {expr[0]}"
    func = OPERATIONS[expr[0]]
    return func(envs, expr[1:])


def main(filename):
    with open(filename, "r") as source_file:
        program = json.load(source_file)
    assert isinstance(program, list)
    envs = [{}]
    result = do(envs, program)


# Create the general foundation of shape class
Shape = {
    "density": do_shape_density,
    "_classname": "Shape",
    "_parent": None,
    "_new": do_shape_new
}

# Create the general foundation of square class and define its parent
Square = {
    "area": do_square_area,
    "_classname": "Square",
    "_parent": Shape,
    "_new": do_square_new
}

# Create the general foundation of circle class and define its parent
Circle = {
    "area": do_circle_area,
    "_classname": "Circle",
    "_parent": Shape,
    "_new": do_circle_new
}

OPERATIONS = {}


def get_all_operations():
    all_functions = globals()

    # Filter functions that start with "do"
    all_functions = [function_name[3:] for function_name in all_functions if function_name.startswith("do_")]
    for funcs_str in all_functions:
        function = globals()["do_" + funcs_str]
        OPERATIONS[funcs_str] = function


if __name__ == "__main__":
    get_all_operations()
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="The input filename")
    parser.add_argument("--trace", help="Enable tracing")
    args = parser.parse_args()

    logger_file = args.trace

    main(args.filename)
