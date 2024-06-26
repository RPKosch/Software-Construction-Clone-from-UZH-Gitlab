from architecture import RAM_LEN
from assembler import Assembler, main

class DataAllocator(Assembler):

    # [assemble]
    DIVIDER = ".data"

    def assemble(self, lines):
        lines = self._get_lines(lines)
        #new split
        to_compile, to_allocate = self._split(lines)
        print("To Compile:")
        print(to_compile)
        print("To Allocate:")
        print(to_allocate)

        labels = self._find_labels(lines)
        print("Labels:")
        print(labels)
        instructions = [ln for ln in to_compile if not self._is_label(ln)]

        #new
        base_of_data = len(instructions)
        self._add_allocations(base_of_data, labels, to_allocate)
        print("Labels after allocations:")
        print(labels)


        compiled = [self._compile(instr, labels) for instr in instructions]
        program = self._to_text(compiled)
        return program

    def _split(self, lines):
        try:
            split = lines.index(self.DIVIDER)
            return lines[0:split], lines[split + 1:]
        except ValueError:
            return lines, []
    # [/assemble]

    # [allocate]
    def _add_allocations(self, base_of_data, labels, to_allocate):
        for alloc in to_allocate:
            fields = [a.strip() for a in alloc.split(":")]
            assert len(fields) == 2, f"Invalid allocation directive '{alloc}'"
            lbl, num_words_text = fields
            assert lbl not in labels, f"Duplicate label '{lbl}' in allocation"
            num_words = int(num_words_text)
            assert (base_of_data + num_words) < RAM_LEN, \
                f"Allocation '{lbl}' requires too much memory"
            labels[lbl] = base_of_data
            base_of_data += num_words
    # [/allocate]


# [main]
if __name__ == "__main__":
    main(DataAllocator)
# [/main]
