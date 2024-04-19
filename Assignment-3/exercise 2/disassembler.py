import sys
from architecture import OPS


# [class]
class Disassembler:
    #main function for what needs to happen
    def disassemble(self, lines):
        lines = self._get_lines(lines)
        instructions = self._get_instructions(lines)
        assembly = self._get_assembly(instructions)
        return assembly
    # edit lines so the disassembler has clean text to work with
    def _get_lines(self, lines):
        lines = [ln.strip() for ln in lines]
        lines = [ln for ln in lines if len(ln) > 0]
        return lines
    # responsible for transforming machine code to OPS code
    def _get_instructions(self, lines):
        instructions = []
        for line in lines:
            line = self._decode(line)
            instruction = self._get_instructions_from_OPS(line[0])
            name = instruction["name"]
            var1 = line[1]
            var2 = line[2]
            ops_type = instruction["fmt"]
            instructions.append([name, var1, var2, ops_type])
        return instructions
    # decodes string into 3 ints
    def _decode(self, line):
        # starting at the back because we switched it while assembling
        return [int(line[4:6], 16), int(line[2:4], 16), int(line[0:2], 16)]
    # iterate through operations to get the desired OPS code
    def _get_instructions_from_OPS(self, wanted):
        all_ops = OPS.items()
        for ops in all_ops:
            ops_code = int(ops[1]["code"])
            if ops_code == wanted:
                return {"name": ops[0], "fmt": ops[1]["fmt"]}  # [name, fmt]
        return None
    # Convert OPS code into assembly code
    def _get_assembly(self, instructions):
        program = []
        label_counter = 0

        for instructions in instructions:
            new_line = f"{instructions[0]}"
            # first operand
            if instructions[3].startswith("r"):
                new_line += (f" R{instructions[1]}")
            # second operand
            if instructions[3].endswith("r"):
                new_line += (f" R{instructions[2]}")
            elif instructions[3].endswith("v"):
                # is a label:
                if instructions[0] in ("beq", "bne"):
                    label_counter += 1
                    program.insert(instructions[2] + label_counter - 1, f"loop{label_counter}:")  # insert label
                    new_line += f" @loop{label_counter}"
                else:
                    new_line += (f" {instructions[2]}")
            program.append(new_line)
        return program

def main(disassembler):
    assert len(sys.argv) == 3, f"Usage: {sys.argv[0]} input  output"
    reader = open(sys.argv[1], "r") if (sys.argv[1] != "-") else sys.stdin
    writer = open(sys.argv[2], "w") if (sys.argv[2] != "-") else sys.stdout
    lines = reader.readlines()
    disassembler = disassembler()
    program = disassembler.disassemble(lines)
    for instruction in program:
        print(instruction, file=writer)


if __name__ == "__main__":
    main(Disassembler)