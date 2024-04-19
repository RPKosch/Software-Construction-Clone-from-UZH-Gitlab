import argparse
import pprint
import file_manager
import os
import time

#setup and teardown implementation

def setup_nothing():
    return 0

def setup_with_text():
    with open("temp.txt", "w") as f:
        f.write("test")


def setup_without_text():
    with open("temp.txt", "w") as f:
        f.write("")


def teardown():
    if os.path.exists("temp.txt"):
        os.remove("temp.txt")


#test for read


def test_read_with_text():
    setup_with_text()
    actual_output = file_manager.read_file("temp.txt")
    expected_output = "test"

    assert actual_output == expected_output

    teardown()


def test_read_without_text():
    setup_without_text()
    actual_output = file_manager.read_file("temp.txt")
    expected_output = ""

    assert actual_output == expected_output
    teardown()


#test create file


def test_create_file():
    setup_nothing()
    file_manager.create_file("temp.txt", content="Testing")
    if os.path.exists("temp.txt"):
        indicator = True
    else:
        indicator = False
    exp_indicator = True

    assert indicator == exp_indicator
    teardown()


def test_create_empty_file():
    setup_nothing()
    file_manager.create_file("temp.txt", content="")
    if os.path.exists("temp.txt"):
        indicator = True
    else:
        indicator = False
    exp_indicator = True

    assert indicator == exp_indicator
    teardown()


def test_write_empty():
    setup_without_text()
    file_manager.write_file("temp.txt","")
    with open("temp.txt", 'r') as file:
        content = file.read()
    exp_content = ""

    assert content == exp_content
    teardown()


def test_write_string():
    setup_without_text()
    file_manager.write_file("temp.txt", "Dies ist ein Test")
    with open("temp.txt", 'r') as file:
        content = file.read()
    exp_content = "Dies ist ein Test"

    assert content == exp_content
    teardown()

def test_delete_empty():
    setup_without_text()
    file_manager.delete_file("temp.txt")

    if not os.path.exists("temp.txt"):
        indicator = True

    exp_indicator = True

    assert indicator == exp_indicator

def test_delete_string():
    setup_with_text()
    file_manager.delete_file("temp.txt")

    if not os.path.exists("temp.txt"):
        indicator = True

    exp_indicator = True

    assert indicator == exp_indicator



def test_write_string():
    setup_without_text()
    file_manager.write_file("temp.txt", "Dies ist ein Test")
    with open("temp.txt", 'r') as file:
        content = file.read()
    exp_content = "Dies ist ein Test"

    assert content == exp_content
    teardown()


def run_tests():
    select_pattern = None
    results = {"pass": 0, "fail": 0, "error": 0}
    parser = argparse.ArgumentParser(description='Run custom tests with optional selection by name pattern.')
    parser.add_argument('--select', help='Select tests by name pattern', required=False)

    args = parser.parse_args()
    select_pattern = args.select

    start_time = time.time()

    for (name, test) in globals().items():
        if not name.startswith("test_"):
            continue
        if (select_pattern == None):
            try:
                test()
                results["pass"] += 1
                print(f"Test: {str(name)} passed\nExecution time: {'%s seconds' % (time.time() - start_time)} \n")
            except AssertionError:
                results["fail"] += 1
                print(f"Test: {name} threw an Assertion Error\nExecution time: {'%s seconds' % (time.time() - start_time)} \n")
            except Exception:
                results["error"] += 1
                print(f"Test: {name} threw an Error\nExecution time: {'%s seconds' % (time.time() - start_time)} \n")

        else:
            if select_pattern in name:
                try:
                    test()
                    results["pass"] += 1
                    print(f"Test: {str(name)} passed\nExecution time: {'%s seconds' % (time.time() - start_time)} \n")
                except AssertionError:
                    results["fail"] += 1
                    print(f"Test: {name} threw an Assertion Error\nExecution time: {'%s seconds' % (time.time() - start_time)} \n")
                except Exception:
                    results["error"] += 1
                    print(f"Test: {name} threw an Error\nExecution time: {'%s seconds' % (time.time() - start_time)} \n")
            else:
                continue

    print("Summary:")
    print(f"pass {results['pass']}")
    print(f"fail {results['fail']}")
    print(f"error {results['error']}")


def find_tests(prefix):
    tests = []
    for (name, func) in globals().items():
        if name.startswith(prefix):
            tests.append(func)
    return tests

run_tests()

#parser = argparse.ArgumentParser(description='Run custom tests with optional selection by name pattern.')
#parser.add_argument('--select', help='Select tests by name pattern', required=False)

#args = parser.parse_args()
#select_pattern = args.select

#run_tests(select_pattern)
