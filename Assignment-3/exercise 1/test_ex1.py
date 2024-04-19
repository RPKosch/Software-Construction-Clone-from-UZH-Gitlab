import os
from arrays import Assembler
from vm import VirtualMachine


def test_insert_values():
    assembler = Assembler()
    reader = open("test_insert_values.as", "r")
    writer = open("test_insert_values_tmp.mx", "w")
    lines = reader.readlines()
    lines = assembler._get_lines(lines)
    program = assembler.assemble(lines)
    for instruction in program:
        print(instruction, file=writer)
    reader_test = open("test_insert_values_tmp.mx", "r")
    lines_test = reader_test.readlines()
    lines_test = assembler._get_lines(lines_test)

    reader_sol = open("test_insert_values_sol.mx", "r")
    lines_sol = reader_test.readlines()
    lines_sol = assembler._get_lines(lines_test)
    assert lines_test == lines_sol

    if os.path.isfile("test_insert_values_tmp.mx"):
        reader_test.close()
        writer.close()
        os.remove("test_insert_values_tmp.mx")
    writer.close()


def test_copy_register():
    assembler = Assembler()
    reader = open("test_copy_register.as", "r")
    writer = open("test_copy_register_tmp.mx", "w")
    lines = reader.readlines()
    lines = assembler._get_lines(lines)
    program = assembler.assemble(lines)
    for instruction in program:
        print(instruction, file=writer)
    reader_test = open("test_copy_register_tmp.mx", "r")
    lines_test = reader_test.readlines()
    lines_test = assembler._get_lines(lines_test)

    reader_sol = open("test_copy_register_sol.mx", "r")
    lines_sol = reader_test.readlines()
    lines_sol = assembler._get_lines(lines_test)
    assert lines_test == lines_sol

    if os.path.isfile("test_copy_register_tmp.mx"):
        reader_test.close()
        writer.close()
        os.remove("test_copy_register_tmp.mx")
    writer.close()


def test_sub():
    assembler = Assembler()
    reader = open("test_sub.as", "r")
    writer = open("test_sub_tmp.mx", "w")
    lines = reader.readlines()
    lines = assembler._get_lines(lines)
    program = assembler.assemble(lines)
    for instruction in program:
        print(instruction, file=writer)
    reader_test = open("test_sub_tmp.mx", "r")
    lines_test = reader_test.readlines()
    lines_test = assembler._get_lines(lines_test)

    reader_sol = open("test_sub_sol.mx", "r")
    lines_sol = reader_test.readlines()
    lines_sol = assembler._get_lines(lines_test)
    assert lines_test == lines_sol

    if os.path.isfile("test_sub_tmp.mx"):
        reader_test.close()
        writer.close()
        os.remove("test_sub_tmp.mx")
    writer.close()


def test_add():
    assembler = Assembler()
    reader = open("test_add.as", "r")
    writer = open("test_add_tmp.mx", "w")
    lines = reader.readlines()
    lines = assembler._get_lines(lines)
    program = assembler.assemble(lines)
    for instruction in program:
        print(instruction, file=writer)
    reader_test = open("test_add_tmp.mx", "r")
    lines_test = reader_test.readlines()
    lines_test = assembler._get_lines(lines_test)

    reader_sol = open("test_add_sol.mx", "r")
    lines_sol = reader_test.readlines()
    lines_sol = assembler._get_lines(lines_test)
    assert lines_test == lines_sol

    if os.path.isfile("test_add_tmp.mx"):
        reader_test.close()
        writer.close()
        os.remove("test_add_tmp.mx")
    writer.close()


def test_print_memory():
    assembler = Assembler()
    reader = open("test_print_memory.as", "r")
    writer = open("test_print_memory_tmp.mx", "w")
    lines = reader.readlines()
    lines = assembler._get_lines(lines)
    program = assembler.assemble(lines)
    for instruction in program:
        print(instruction, file=writer)
    reader_test = open("test_print_memory_tmp.mx", "r")
    lines_test = reader_test.readlines()
    lines_test = assembler._get_lines(lines_test)

    reader_sol = open("test_print_memory_sol.mx", "r")
    lines_sol = reader_test.readlines()
    lines_sol = assembler._get_lines(lines_test)
    assert lines_test == lines_sol

    if os.path.isfile("test_print_memory_tmp.mx"):
        reader_test.close()
        writer.close()
        os.remove("test_print_memory_tmp.mx")
    writer.close()


def test_load_register():
    assembler = Assembler()
    reader = open("test_load_register.as", "r")
    writer = open("test_load_register_tmp.mx", "w")
    lines = reader.readlines()
    lines = assembler._get_lines(lines)
    program = assembler.assemble(lines)
    for instruction in program:
        print(instruction, file=writer)
    reader_test = open("test_load_register_tmp.mx", "r")
    lines_test = reader_test.readlines()
    lines_test = assembler._get_lines(lines_test)

    reader_sol = open("test_load_register_sol.mx", "r")
    lines_sol = reader_test.readlines()
    lines_sol = assembler._get_lines(lines_test)
    assert lines_test == lines_sol

    if os.path.isfile("test_load_register_tmp.mx"):
        reader_test.close()
        writer.close()
        os.remove("test_load_register_tmp.mx")
    writer.close()


def test_branch_equal():
    assembler = Assembler()
    reader = open("test_branch_equal.as", "r")
    writer = open("test_branch_equal_tmp.mx", "w")
    lines = reader.readlines()
    lines = assembler._get_lines(lines)
    program = assembler.assemble(lines)
    for instruction in program:
        print(instruction, file=writer)
    reader_test = open("test_branch_equal_tmp.mx", "r")
    lines_test = reader_test.readlines()
    lines_test = assembler._get_lines(lines_test)

    reader_sol = open("test_branch_equal_sol.mx", "r")
    lines_sol = reader_test.readlines()
    lines_sol = assembler._get_lines(lines_test)
    assert lines_test == lines_sol

    if os.path.isfile("test_branch_equal_tmp.mx"):
        reader_test.close()
        writer.close()
        os.remove("test_branch_equal_tmp.mx")
    writer.close()


def test_branch_not_equal():
    assembler = Assembler()
    reader = open("test_branch_not_equal.as", "r")
    writer = open("test_branch_not_equal_tmp.mx", "w")
    lines = reader.readlines()
    lines = assembler._get_lines(lines)
    program = assembler.assemble(lines)
    for instruction in program:
        print(instruction, file=writer)
    reader_test = open("test_branch_not_equal_tmp.mx", "r")
    lines_test = reader_test.readlines()
    lines_test = assembler._get_lines(lines_test)

    reader_sol = open("test_branch_not_equal_sol.mx", "r")
    lines_sol = reader_test.readlines()
    lines_sol = assembler._get_lines(lines_test)
    assert lines_test == lines_sol

    if os.path.isfile("test_branch_not_equal_tmp.mx"):
        reader_test.close()
        writer.close()
        os.remove("test_branch_not_equal_tmp.mx")
    writer.close()


#Testing for VM

def test_insert_values_vm():
    readerfile = "test_insert_values_sol.mx"
    writerfile = readerfile[:-6] + "tmp.mx"
    solutionfile = readerfile[:-3] + "_vm.mx"

    terminalinput = f"python vm.py {readerfile} {writerfile}"
    os.system(terminalinput)

    reader_test = open(writerfile, "r")  # was ich auasfèhren will
    lines_test = reader_test.readlines()
    print(f"my output: {lines_test}")
    reader_sol = open(solutionfile, "r")
    lines_sol = reader_sol.readlines()
    print(f"my solution: {lines_sol}")
    assert lines_test == lines_sol

    if os.path.isfile(writerfile):
        reader_test.close()
        reader_sol.close()
        os.remove(writerfile)


def test_copy_register_vm():
    readerfile = "test_insert_values_sol.mx"
    writerfile = readerfile[:-6] + "tmp.mx"
    solutionfile = readerfile[:-3] + "_vm.mx"

    terminalinput = f"python vm.py {readerfile} {writerfile}"
    os.system(terminalinput)

    reader_test = open(writerfile, "r")  # was ich auasfèhren will
    lines_test = reader_test.readlines()
    print(f"my output: {lines_test}")
    reader_sol = open(solutionfile, "r")
    lines_sol = reader_sol.readlines()
    print(f"my solution: {lines_sol}")
    assert lines_test == lines_sol

    if os.path.isfile(writerfile):
        reader_test.close()
        reader_sol.close()
        os.remove(writerfile)


def test_add_vm():
    readerfile = "test_add_sol.mx"
    writerfile = readerfile[:-6] + "tmp.mx"
    solutionfile = readerfile[:-3] + "_vm.mx"

    terminalinput = f"python vm.py {readerfile} {writerfile}"
    os.system(terminalinput)

    reader_test = open(writerfile, "r")
    lines_test = reader_test.readlines()
    print(f"my output: {lines_test}")
    reader_sol = open(solutionfile, "r")
    lines_sol = reader_sol.readlines()
    print(f"my solution: {lines_sol}")
    assert lines_test == lines_sol

    if os.path.isfile(writerfile):
        reader_test.close()
        reader_sol.close()
        os.remove(writerfile)


def test_sub_vm():
    readerfile = "test_sub_sol.mx"
    writerfile = readerfile[:-6] + "tmp.mx"
    solutionfile = readerfile[:-3] + "_vm.mx"

    terminalinput = f"python vm.py {readerfile} {writerfile}"
    os.system(terminalinput)

    reader_test = open(writerfile, "r")
    lines_test = reader_test.readlines()
    print(f"my output: {lines_test}")
    reader_sol = open(solutionfile, "r")
    lines_sol = reader_sol.readlines()
    print(f"my solution: {lines_sol}")
    assert lines_test == lines_sol

    if os.path.isfile(writerfile):
        reader_test.close()
        reader_sol.close()
        os.remove(writerfile)


def test_print_memory_vm():
    readerfile = "test_print_memory_sol.mx"
    writerfile = readerfile[:-6] + "tmp.mx"
    solutionfile = readerfile[:-3] + "_vm.mx"

    terminalinput = f"python vm.py {readerfile} {writerfile}"
    os.system(terminalinput)

    reader_test = open(writerfile, "r")
    lines_test = reader_test.readlines()
    print(f"my output: {lines_test}")
    reader_sol = open(solutionfile, "r")
    lines_sol = reader_sol.readlines()
    print(f"my solution: {lines_sol}")
    assert lines_test == lines_sol

    if os.path.isfile(writerfile):
        reader_test.close()
        reader_sol.close()
        os.remove(writerfile)


def test_load_register_vm():
    readerfile = "test_load_register_sol.mx"
    writerfile = readerfile[:-6] + "tmp.mx"
    solutionfile = readerfile[:-3] + "_vm.mx"

    terminalinput = f"python vm.py {readerfile} {writerfile}"
    os.system(terminalinput)

    reader_test = open(writerfile, "r")
    lines_test = reader_test.readlines()
    print(f"my output: {lines_test}")
    reader_sol = open(solutionfile, "r")
    lines_sol = reader_sol.readlines()
    print(f"my solution: {lines_sol}")
    assert lines_test == lines_sol

    if os.path.isfile(writerfile):
        reader_test.close()
        reader_sol.close()
        os.remove(writerfile)


def test_branch_equal_vm():
    readerfile = "test_branch_equal_sol.mx"
    writerfile = readerfile[:-6] + "tmp.mx"
    solutionfile = readerfile[:-3] + "_vm.mx"

    terminalinput = f"python vm.py {readerfile} {writerfile}"
    os.system(terminalinput)

    reader_test = open(writerfile, "r")
    lines_test = reader_test.readlines()
    print(f"my output: {lines_test}")
    reader_sol = open(solutionfile, "r")
    lines_sol = reader_sol.readlines()
    print(f"my solution: {lines_sol}")
    assert lines_test == lines_sol

    if os.path.isfile(writerfile):
        reader_test.close()
        reader_sol.close()
        os.remove(writerfile)


def test_branch_not_equal_vm():
    readerfile = "test_branch_not_equal_sol.mx"
    writerfile = readerfile[:-6] + "tmp.mx"
    solutionfile = readerfile[:-3] + "_vm.mx"

    terminalinput = f"python vm.py {readerfile} {writerfile}"
    os.system(terminalinput)

    reader_test = open(writerfile, "r")
    lines_test = reader_test.readlines()
    print(f"my output: {lines_test}")
    reader_sol = open(solutionfile, "r")
    lines_sol = reader_sol.readlines()
    print(f"my solution: {lines_sol}")
    assert lines_test == lines_sol

    if os.path.isfile(writerfile):
        reader_test.close()
        reader_sol.close()
        os.remove(writerfile)
#Testing C

def test_out_of_memory():
    assembler = Assembler()
    reader = open("test_out_of_memory.as", "r")
    lines = reader.readlines()
    try:
        lines = assembler._get_lines(lines)
        program = assembler.assemble(lines)
    except(KeyError):
        reader.close()
        assert True
    else:
        reader.close()
        assert False


def test_instructions_not_found_as():
    assembler = Assembler()
    reader = open("test_instructions_not_found.as", "r")
    lines = reader.readlines()
    try:
        lines = assembler._get_lines(lines)
        program = assembler.assemble(lines)
    except(KeyError):
        reader.close()
        assert True
    else:
        reader.close()
        assert False


def test_instructions_not_found_vm():
    vm = VirtualMachine()
    reader = open("test_instructions_not_found_vm.mx", "r")

    try:
        lines = [ln.strip() for ln in reader.readlines()]
        program = [int(ln, 16) for ln in lines if len(ln) > 0]
        vm.initialize(program)
        vm.run()
    except(AssertionError):
        reader.close()
        assert True
    else:
        reader.close
        assert False
