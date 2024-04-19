import datetime
import random

all_id = {} # All ID's will be saved in this global dictionary
#enable_tracing = False  # Global flag to enable or disable tracing
logger_file = None


def set_tracing(enable):
    global enable_tracing
    enable_tracing = enable


def set_logger_file(file):
    global logger_file
    logger_file = file


def generate_id():
    while True:
        new_id = random.randint(1, 1000000)
        if new_id not in all_id.keys():
            all_id[new_id] = True
            return new_id


# Outer Function to import additional data. In this case the logger_file

def trace_function(function):
    # trace_function function is used that no infinite recursion is happening
        # _inner function what should happen around the functions that were already created
    def _inner(*args, **kwargs):
        if logger_file:
            if all_id == {}:
                with open(logger_file, "a") as file:
                    file.write(f"id,function_name,event,timestamp\n")
                    file.flush()

            with open(logger_file, "a") as file:
                function_name = args[1][0]
                status = 'start'
                current_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')

    # create a id funciton that won't repete the same function. preferably form 1-1 Million
                unique_id = generate_id()

                # Logging before the function has run
                file.write(f"{unique_id},{function_name},{status},{current_time}\n")
                file.flush()

                output = function(*args, **kwargs)

                status = 'stop'
                current_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')

                # Logging after the function has run
                file.write(f"{unique_id},{function_name},{status},{current_time}\n")
                file.flush()

                return output
        else:
            output = function(*args, **kwargs)
            return output
    return _inner



