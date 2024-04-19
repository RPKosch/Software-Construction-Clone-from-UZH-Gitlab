import os
import test_dis
from disassembler import Disassembler


def test_count_up():
    disassembler = Disassembler()
    reader = open("examplle.mx", "r")
    writer = open("test1.as", "w")
    lines = reader.readlines()
    lines = disassembler._get_lines(lines)
    program = disassembler.disassemble(lines)
    for instruction in program:
        print(instruction, file=writer)
    reader_test = open("test1.as", "r")
    lines_test = reader_test.readlines()
    lines_test = disassembler._get_lines(lines_test)

    reader_sol = open("count_up.as", "r")
    lines_sol = reader_test.readlines()
    lines_sol = disassembler._get_lines(lines_test)

    assert lines_test == lines_sol


    if os.path.isfile("test1.as"):
        reader_test.close()
        writer.close()
        os.remove("test1.as")
    writer.close()

def test_simple_print():
    disassembler = Disassembler()
    reader = open("example2.mx", "r")
    writer = open("test2.as", "w")
    lines = reader.readlines()
    lines = disassembler._get_lines(lines)
    program = disassembler.disassemble(lines)
    for instruction in program:
        print(instruction, file=writer)
    reader_test = open("test2.as", "r")
    lines_test = reader_test.readlines()
    lines_test = disassembler._get_lines(lines_test)

    reader_sol = open("example2.as", "r")
    lines_sol = reader_test.readlines()
    lines_sol = disassembler._get_lines(lines_test)

    assert lines_test == lines_sol

    if os.path.isfile("test2.as"):
        reader_test.close()
        writer.close()
        os.remove("test2.as")
    writer.close()


def test_simple_print_2():
    disassembler = Disassembler()
    reader = open("example3.mx", "r")
    writer = open("test3.as", "w")
    lines = reader.readlines()
    lines = disassembler._get_lines(lines)
    program = disassembler.disassemble(lines)
    for instruction in program:
        print(instruction, file=writer)
    reader_test = open("test3.as", "r")
    lines_test = reader_test.readlines()
    lines_test = disassembler._get_lines(lines_test)

    reader_sol = open("example3.as", "r")
    lines_sol = reader_test.readlines()
    lines_sol = disassembler._get_lines(lines_test)

    assert lines_test == lines_sol

    if os.path.isfile("test3.as"):
        reader_test.close()
        writer.close()
        os.remove("test3.as")
    writer.close()

def test_faulty_mx():
    disassembler = Disassembler()
    reader = open("example4.mx", "r")
    writer = open("test4.as", "w")
    lines = reader.readlines()
    lines = disassembler._get_lines(lines)
    program = disassembler.disassemble(lines)
    for instruction in program:
        print(instruction, file=writer)
    reader_test = open("test4.as", "r")
    lines_test = reader_test.readlines()
    lines_test = disassembler._get_lines(lines_test)

    reader_sol = open("count_up.as", "r")
    lines_sol = reader_test.readlines()
    lines_sol = disassembler._get_lines(lines_test)

    assert lines_test == lines_sol

    if os.path.isfile("test4.as"):
        reader_test.close()
        writer.close()
        os.remove("test4.as")
    writer.close()
