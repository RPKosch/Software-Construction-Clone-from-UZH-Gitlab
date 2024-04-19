NUM_REG = 4  # number of registers
RAM_LEN = 256  # number of words in RAM

OPS = {
    "hlt": {"code": 0x1, "fmt": "--"},  # Halt program check
    "ldc": {"code": 0x2, "fmt": "rv"},  # Load value check
    "ldr": {"code": 0x3, "fmt": "rr"},  # Load register  check
    "cpy": {"code": 0x4, "fmt": "rr"},  # Copy register check
    "str": {"code": 0x5, "fmt": "rr"},  # Store register check
    "add": {"code": 0x6, "fmt": "rr"},  # Add check
    "sub": {"code": 0x7, "fmt": "rr"},  # Subtract check
    "beq": {"code": 0x8, "fmt": "rv"},  # Branch if equal check
    "bne": {"code": 0x9, "fmt": "rv"},  # Branch if not equal check
    "prr": {"code": 0xA, "fmt": "r-"},  # Print register check
    "prm": {"code": 0xB, "fmt": "r-"},  # Print memory check
    "inc": {"code": 0xC, "fmt": "r-"},  # increment by 1 - only register
    "dec": {"code": 0xD, "fmt": "r-"},  # decrement by 1 - only register
    "swp": {"code": 0xE, "fmt": "rr"},  # decrement by 1 - two register
}

OP_MASK = 0xFF  # select a single byte
OP_SHIFT = 8  # shift up by one byte
OP_WIDTH = 6  # op width in characters when printing
