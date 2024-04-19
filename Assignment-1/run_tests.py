import file_manager
import os
import argparse
import re
import time as t


# Setup - We need only one file with text and one clear file to test everything.
# Those are the two types of good paths for programming.
# We as programmers are thinking that those two are the most common inputs.
# We will also check bad paths but we don't need a setup for that.


def setup():
    with open("temp_without_text.txt", "w") as f:
        f.write("")
    with open("temp_with_text.txt", "w") as f:
        f.write("test")


# Teardown - We need to delete all created files.
# Before deleting we need to check if they still exist. Else an error would occur.
# We need another deletion for the possibly created files for the creation tests

def teardown():
    if os.path.exists("temp_without_text.txt"):
        os.remove("temp_without_text.txt")
    if os.path.exists("temp_with_text.txt"):
        os.remove("temp_with_text.txt")
    if os.path.exists("temp_file.txt"):
        os.remove("temp_file.txt")
    if os.path.exists("temp_file.pdf"):
        os.remove("temp_file.pdf")


# 3 Tests for the read function.
# First two are for good path testing. The file is either clear or has already texts.
# The Third is tested because there could be possible input errors.

def test_read_with_text():
    setup()
    actual_output = file_manager.read_file("temp_with_text.txt")
    expected_output = "test"
    assert actual_output == expected_output
    teardown()


def test_read_without_text():
    setup()
    actual_output = file_manager.read_file("temp_without_text.txt")
    expected_output = ""
    assert actual_output == expected_output
    teardown()


def test_read_text_with_wrong_file():
    setup()
    actual_output = file_manager.read_file("temp_does_not_exist.txt")
    expected_output = None
    assert actual_output == expected_output
    teardown()


# All tests for creation of a new file
# The two only good path are when a correct file name is given with or without content.
# Additionally, we test an invalid input with a non txt file.
# We also check what happens when the text file already exists.


def test_create_file():
    checker = file_manager.create_file("temp_file.txt", content="Testing")
    if os.path.exists("temp_file.txt"):
        indicator = True
    else:
        indicator = False

    assert checker == indicator
    teardown()


def test_create_empty_file():
    checker = file_manager.create_file("temp_file.txt", content="")
    if os.path.exists("temp_file.txt"):
        indicator = True
    else:
        indicator = False

    assert checker == indicator
    teardown()


def test_create_a_pdf_file():
    checker = file_manager.create_file("temp_file.pdf", content="")
    if os.path.exists("temp_file.pdf"):
        indicator = True
    else:
        indicator = False

    assert checker == indicator
    teardown()


def test_create_with_a_existing_file():
    checker = file_manager.create_file("temp_with_text.txt", content="")
    if os.path.exists("temp_with_text.txt"):
        indicator = True
    else:
        indicator = False

    assert checker == indicator
    teardown()


# All tests for writing something into a file
# We test the good paths where a file already exists with and without written text.
# And then we check if it handles a none existing file name.


def test_write_from_new():
    setup()
    checker = file_manager.write_file("temp_without_text.txt", "New")
    with open("temp_without_text.txt", "r") as f:
        actual_output = f.read()
    expected_output = "New"

    if actual_output == expected_output:
        indicator = True
    else:
        indicator = False
    assert checker == indicator
    teardown()


# The write function overwrites existing text. Therefore, the expected output is also "New".
def test_write_from_existing():
    setup()
    checker = file_manager.write_file("temp_with_text.txt", "New")
    with open("temp_with_text.txt", "r") as f:
        actual_output = f.read()
    expected_output = "New"

    if actual_output == expected_output:
        indicator = True
    else:
        indicator = False
    assert checker == indicator
    teardown()


# Works properly because the write function also creates the file.

def test_write_with_not_existing_file():
    setup()
    checker = file_manager.write_file("temp_does_not_exist.txt", "New")
    with open("temp_does_not_exist.txt", "r") as f:
        actual_output = f.read()
    expected_output = "New"

    if actual_output == expected_output:
        indicator = True
    else:
        indicator = False
    assert checker == indicator
    teardown()


# All deletion test
# We check again first the valid inputs.
# Therefore, we test for a file with and without text.
# Then we check again for a not existing file.


def test_deletion_without_test():
    setup()
    checker = file_manager.delete_file("temp_without_text.txt")
    if os.path.exists("temp_without_text.txt"):
        indicator = False
    else:
        indicator = True
    assert checker == indicator
    teardown()


def test_deletion_with_test():
    setup()
    checker = file_manager.delete_file("temp_with_text.txt")
    if os.path.exists("temp_with_text.txt"):
        indicator = False
    else:
        indicator = True
    assert checker == indicator
    teardown()


def test_deletion_with_non_existing_file():
    setup()
    checker = file_manager.delete_file("temp_does_not_exist.txt")
    if os.path.exists("temp_does_not_exist.txt"):
        indicator = False
    else:
        indicator = True
    assert checker == indicator
    teardown()


def run_tests():
    parser = argparse.ArgumentParser()
    parser.add_argument("--select", help="Run only test with this string")
    args = parser.parse_args()
    pattern = args.select
    all_tests = [["Name of Test", "test status", "Time in Seconds"]]
    results = {"pass": 0, "fail": 0, "error": 0}
    # Check for all functions that start with test_
    for (name, test) in globals().items():
        if not name.startswith("test_"):
            continue
        # Check if the pattern is specified and filter tests accordingly
        if pattern and re.search(pattern, name) is None:
            continue

        try:
            start_time = t.time()
            test()
            end_time = t.time()
            information = [name, "pass", end_time - start_time]
            all_tests.append(information)
            results["pass"] += 1
        except AssertionError:
            end_time = t.time()
            results["fail"] += 1
            information = [name, "fail", end_time - start_time]
            all_tests.append(information)
        except Exception:
            end_time = t.time()
            results["error"] += 1
            information = [name, "error", end_time - start_time]
            all_tests.append(information)

    print(f"Pass: {results['pass']}")
    print(f"Fail: {results['fail']}")
    print(f"Error: {results['error']}")
    print("")

    for row in all_tests:
        print('| {:^40} | {:^13} | {:^30} |'.format(*row))


if __name__ == "__main__":
    run_tests()
