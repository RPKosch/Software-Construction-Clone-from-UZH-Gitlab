import argparse
import datetime


def generate_report(trace_file):
    # Dictionary to store function all statistics
    all_functions = {}
    # Dictionary only to count functions
    counter_for_functions = {}

    with open(trace_file, "r") as file:
        # Read all lines from the file
        all_lines = file.readlines()

        # Iterate over each line in the trace file
        for line in all_lines:
            # Extract relevant information from the comma-separated line
            # We use the strip because else we cannot read the timestamp
            unique_id, function_name, status, timestamp = line.strip().split(",")

            # Skip the loop in the first iteration
            if unique_id == "id":
                continue

            # Get the time when the function starts
            if status == "start":
                date_time_obj = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
                start_time = date_time_obj.timestamp()
                # Load the id in for checking how long the function took
                all_functions[unique_id] = [function_name, start_time, 0, 0]

            # Get the time when the functions stop
            elif status == "stop":
                date_time_obj = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
                stop_time = date_time_obj.timestamp()
                # Get the duration of the function and place it on the [3] slot
                all_functions[unique_id][2] = stop_time
                all_functions[unique_id][3] = all_functions[unique_id][2] - all_functions[unique_id][1]

    # Load all the data from the one dictionary to the other to check for how many times the functions were used
    for _, (function_name, start_time, end_time, overall_time) in all_functions.items():
        if function_name in counter_for_functions:
            counter_for_functions[function_name][0] += 1  # Increment the number of calls
            counter_for_functions[function_name][1] += overall_time  # Add execution time
        else:
            counter_for_functions[function_name] = [1, overall_time]

    # Print the report header
    print("|    Function Name     | Num. of calls | Total Time (ms) | Average Time (ms)|")
    print("|---------------------------------------------------------------------------|")

    # Sort functions alphabetically and iterate over them to print the report
    all_functions = dict(sorted(counter_for_functions.items()))
    for function_name, (num_calls, total_time) in all_functions.items():
        # Calculate average time, handling cases where num_calls is zero
        average_time = total_time / num_calls if num_calls > 0 else 0

        # Print the function statistics in a formatted table
        print(f"| {function_name:<20} | {num_calls:^13} | {total_time*1000:^15.3f} | {average_time*1000:^16.3f} |")


# Main entry point of the script
if __name__ == "__main__":
    # Create an argument parser to handle command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="The input filename")
    args = parser.parse_args()

    # Call the generate_report function with the specified filename
    generate_report(args.filename)

