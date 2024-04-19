import sys

from architecture import VMState
from vm_step import VirtualMachineStep


class VirtualMachineExtend(VirtualMachineStep):
    # [init]
    def __init__(self, reader=input, writer=sys.stdout):
        super().__init__(reader, writer)
        self.handlers = {
            "dis": self._do_disassemble,
            "ip": self._do_ip,
            "memory": self._do_memory,
            "quit": self._do_quit,
            "run": self._do_run,
            "step": self._do_step,
        }
    # [/init]

    # [interact]
    def interact(self, addr):
        prompt = "".join(sorted({key[0] for key in self.handlers}))
        interacting = True
        while interacting:
            try:
                command = self.read(f"{addr:06x} [{prompt}]> ")
                
                #checks if input is included in any word of handlers, if it is, sets command to this word
                for ele in self.handlers:
                    try:
                        if command in ele[0:len(command)]:
                            command = ele
                    except IndexError: continue
                if not command:
                    continue
                elif command not in self.handlers:
                    self.write(f"Unknown command {command}")
                else:
                    interacting = self.handlers[command](self.ip)
            except EOFError:
                self.state = VMState.FINISHED
                interacting = False
    # [/interact]

    def _do_disassemble(self, addr):
        self.write(self.disassemble(addr, self.ram[addr]))
        return True

    def _do_ip(self, addr):
        self.write(f"{self.ip:06x}")
        return True

    # [memory]
    def _do_memory(self, addr):
        #get highest memoryaddress
        top = max(i for (i, m) in enumerate(self.ram) if m != 0)
        
        #get user input and seperate it into list by seperating after space
        self.write(f"to input multiple numbers, write space in between, only first two numbers will be used")
        command = self.read(f"{addr:06x} [1234567890]> ")
        num = command.split(" ")
        
        #check if all inputs are numbers
        for ele in num:
            try: int(ele)
            except Exception:
                self.write(f"Memory only accepts numbers, not {ele}")
                return
        
        #if multiple inputs are given, choose first two and write all memories between these addresses
        if len(num) >= 2:
            big = int(num[1])
            small = int(num[0])
            #switch if first number is bigger than second
            if big < small:
                x = small
                small = big
                big = x
            if big > top:
                self.write(f"{big} is a too big Number for memory")
                return
            for i in range(small, big+1):
                self.write(f"{self.ram[i]:06x}")
        
        #if only one input is given, write memory address
        else:
            if int(num[0]) > top:
                self.write(f"{num[0]} is a too big Number for memory")
                return
            self.write(f"{self.ram[int(num[0])]:06x}")
        
        return True
    # [/memory]

    def _do_quit(self, addr):
        self.state = VMState.FINISHED
        return False

    def _do_run(self, addr):
        self.state = VMState.RUNNING
        return False

    # [step]
    def _do_step(self, addr):
        self.state = VMState.STEPPING
        return False
    # [/step]


if __name__ == "__main__":
    VirtualMachineExtend.main()
