import pprint
import file_manager

#here come the tests
#only a test for setup
def test_setup_without_text():
    setup_with_text()
    teardown()
    if os.path.exists("lol.txt"):
        raise Exception
    
def test_setup_with_text():
    setup_without_text()
    teardown()
    if os.path.exists("lol.txt"):
        raise Exception

#tests for read_file function   
def test_read_file_correct():
    setup_with_text()
    expected = "lol"
    real = file_manager.read_file("lol.txt")
    if real != expected:
        raise AssertionError
    teardown()
    
def test_read_file_false():
    setup_with_text()
    expected = "wrong"
    real = file_manager.read_file("lol.txt")
    if real == expected:
        raise AssertionError
    teardown()
    
def test_read_file_no_file():
    setup_with_text()
    real = file_manager.read_file("notreal.txt")
    if real != None:
        raise AssertionError
    teardown()
    
#tests for create_file function
def test_create_file_correct():
    real = file_manager.create_file("lol.txt", "lol")
    if real != True:
        raise AssertionError
    teardown()
    
def test_create_file_overwrite():
    setup_with_text()
    real = file_manager.create_file("lol.txt", "lolyes")
    if real != True:
        raise AssertionError
    teardown()
    
def test_create_file_no_name():
    real = file_manager.create_file("", "lolyes")
    if real != False:
        raise AssertionError
    
#tests for write_file function
def test_write_file_correct():
    setup_without_text()
    real = file_manager.write_file("lol.txt", "good morning")
    if real != True:
        raise AssertionError
    teardown()

def test_write_file_new_file():
    real = file_manager.write_file("lol.txt", "good morning")
    if real != True:
        raise AssertionError
    teardown()
    
def test_write_file_no_name():
    real = file_manager.write_file("", "lolyes")
    if real != False:
        raise AssertionError
    
#tests for delete_file function
def test_delete_file_correct():
    setup_with_text()
    real = file_manager.delete_file("lol.txt")
    if real != True:
        raise AssertionError
    
def test_delete_file_no_file():
    real = file_manager.delete_file("lol.txt")
    if real != False:
        raise AssertionError
    
    
def run_tests():
    results = {"pass": 0, "fail": 0, "error": 0}
    for (name, test) in globals().items():
        if not name.startswith("test_"):
            continue
        try:
            test()
            results["pass"] += 1
        except AssertionError:
            results["fail"] += 1
        except Exception:
            results["error"] += 1
    print(f"pass {results['pass']}")
    print(f"fail {results['fail']}")
    print(f"error {results['error']}")

run_tests()