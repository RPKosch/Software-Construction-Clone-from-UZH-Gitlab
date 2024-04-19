import sys

from architecture import OPS, VMState
from vm_extend import VirtualMachineExtend


class VirtualMachineBreak(VirtualMachineExtend):
    # [init]
    def __init__(self):
        super().__init__()
        self.breaks = {}
        self.watchpoints = []
        self.handlers |= {
            "break": self._do_add_breakpoint,
            "clear": self._do_clear_breakpoint,
            "watchpoint": self._do_watchpoint,
        }
    # [/init]

    # [show]
    def show(self):
        super().show()
        if self.breaks:
            self.write("-" * 6)
            for key, instruction in self.breaks.items():
                self.write(f"{key:06x}: {self.disassemble(key, instruction)}")
    # [/show]

    # [run]
    def run(self):
        self.state = VMState.STEPPING
        while self.state != VMState.FINISHED:
            instruction = self.ram[self.ip]
            op, arg0, arg1 = self.decode(instruction)

            if op == OPS["brk"]["code"]:
                original = self.breaks[self.ip]
                op, arg0, arg1 = self.decode(original)
                self.interact(self.ip)
                self.ip += 1
                self.execute(op, arg0, arg1)
            
            #halt the programm if address is a watchpoint
            elif self.ip in self.watchpoints:
                self.write(f"Programm has reached watchpoint at address {self.ip}")
                self.state = VMState.FINISHED

            else:
                if self.state == VMState.STEPPING:
                    self.interact(self.ip)
                self.ip += 1
                self.execute(op, arg0, arg1)
    # [/run]

    # [add]
    def _do_add_breakpoint(self, addr):
        #get highest memoryaddress
        top = max(i for (i, m) in enumerate(self.ram) if m != 0)
        #get input from user
        self.write(f"Don't write anything in terminal if you want to set breakpoint here")
        command = self.read(f"{addr:06x} [1234567890]> ")
        
        #if user didn't input anything, continue at current address
        if command == "":
            if self.ram[addr] == OPS["brk"]["code"]:
                self.write(f"There is already a breakpoint at address {addr}")
                return
            self.breaks[addr] = self.ram[addr]
            self.ram[addr] = OPS["brk"]["code"]
            self.write(f"breakpoint put at address {addr}")
        
        #if user input something, put breakpoint at input address
        else:
            #check for all wrong inputs
            try: int(command)
            except Exception:
                self.write(f"Break only accepts numbers, and not {command}")
                return
            if int(command) > top:
                self.write(f"{command} is a too high number")
                return
            #check if there is already a breakpoint
            if self.ram[int(command)] == OPS["brk"]["code"]:
                self.write(f"There is already a breakpoint at address {int(command)}")
                return
            #set breakpoint
            self.breaks[int(command)] = self.ram[int(command)]
            self.ram[int(command)] = OPS["brk"]["code"]
            self.write(f"breakpoint put at address {int(command)}")
            
        return True
    # [/add]

    # [clear]
    def _do_clear_breakpoint(self, addr):
        #get highest memoryaddress
        top = max(i for (i, m) in enumerate(self.ram) if m != 0)
        #get input from user
        self.write(f"Don't write anything in terminal if you want to clear breakpoint here")
        command = self.read(f"{addr:06x} [1234567890]> ")
        
        #if user didn't input anything, continue at current address
        if command == "":
            if self.ram[addr] != OPS["brk"]["code"]:
                self.write(f"There is no breakpoint at address {addr}")
                return
            self.ram[addr] = self.breaks[addr]
            del self.breaks[addr]
            self.write(f"deleted breakpoint at address {addr}")
            return True
        
        #if user input something, put breakpoint at input address
        else:
            #check for all wrong inputs
            try: int(command)
            except Exception:
                self.write(f"Clear only accepts numbers, and not {command}")
                return
            if int(command) > top:
                self.write(f"{command} is a too high number")
                return
            
            #if there is no breakpoint move on
            if self.ram[int(command)] != OPS["brk"]["code"]:
                self.write(f"There is no breakpoint at address {int(command)}")
                return
            #delete breakpoint
            self.ram[int(command)] = self.breaks[int(command)]
            del self.breaks[int(command)]
            self.write(f"deleted breakpoint at address {int(command)}")
            return True
    # [/clear]
    
    # [/watchpoint]
    def _do_watchpoint(self, addr):
        #get highest memoryaddress
        top = max(i for (i, m) in enumerate(self.ram) if m != 0)
        #get input from user
        self.write(f"Don't write anything in terminal if you want to set watchpoint here")
        command = self.read(f"{addr:06x} [1234567890]> ")
        
        #if user didn't input anything, continue at current address
        if command == "":
            if addr in self.watchpoints:
                self.write(f"{addr} is already a watchpoint")
                return
            self.watchpoints.append(addr)
            self.write(f"Watchpoint put at address {addr}")
        
        #if user input something, put watchpoint at input address
        else:
            #check for all wrong inputs
            try: int(command)
            except Exception:
                self.write(f"Watchpoint only accepts numbers, and not {command}")
                return
            if int(command) > top:
                self.write(f"{command} is a too high number")
                return
            #check if there is already a watchpoint
            if int(command) in self.watchpoints:
                self.write(f"{int(command)} is already a watchpoint")
                return
            #set watchpoint
            self.watchpoints.append(int(command))
            self.write(f"Watchpoint put at address {int(command)}")
            
        return True
    # [/watchpoint]


if __name__ == "__main__":
    VirtualMachineBreak.main()
