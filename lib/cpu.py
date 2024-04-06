"""
The CPU

The CPU is the main component of the console. It is responsible for executing instructions.

## CPU memory map

[ 0x8000, 0xFFFF ]: Cartridge ROM
[ 0x6000, 0x7FFF ]: Cartridge Save RAM (e.g, Zelda had one for internal save states)
[ 0x4020, 0x5FFF ]: Expansion ROM
[ 0x2000, 0x401F ]: Memory-mapped I/O Registers (PPU, APU, gamepads)
[ 0x0000, 0x1FFF ]: CPU 2KB internal RAM

## CPU registers

- Program Counter (PC):
    - address of next instruction
- Stack Pointer (SP):
    - [0x0100 .. 0x1FF]
    - points to the top stack location in memory
- Accumulator (A):
    - results of arithmetic, logic, and memory access operations
    - can be used for input operator
- Register X (X)
- Register Y (Y)
- Processor status (P) -
    - 8-bit register represents 7 status flags

    NV1B DIZC
    |||| ||||
    |||| |||+- Carry
    |||| ||+-- Zero
    |||| |+--- Interrupt Disable
    |||| +---- Decimal
    |||+------ (No CPU effect; see: the B flag)
    ||+------- (No CPU effect; always pushed as 1)
    |+-------- Overflow
    +--------- Negative

"""

from datetime import datetime

class CPU:
    def __init__(self) -> None:

        # using explicit bytes for clarity and info
        self.program_counter = 0x0000
        self.stack_pointer = 0x00
        self.accumulator = 0x00
        self.register_x = 0x00
        self.register_y = 0x00
        self.processor_status = 0x00

    def interpret(self, program) -> None:
        self.program_counter = 0

    def _state(self) -> None:
        formatted_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("--------------------------------------")
        print(f"{formatted_now} [haiiro] CPU State")
        print("--------------------------------------")
        print(f"PC:\t0x{format(self.program_counter, '04x')}")
        print(f"SP:\t0x{format(self.stack_pointer, '02x')}")
        print(f"A:\t0x{format(self.accumulator, '02x')}")
        print(f"X:\t0x{format(self.register_x, '02x')}")
        print(f"Y:\t0x{format(self.register_y, '02x')}")
        print(f"\nP:\t{format(self.processor_status, '08b')} (NV1BDIZC)")
        print(f"\tN: {(self.processor_status & 0b10000000) >> 7}\tV: {(self.processor_status & 0b01000000) >> 6}\t1: {(self.processor_status & 0b00100000) >> 5}\tB: {(self.processor_status & 0b00010000) >> 4}")
        print(f"\tD: {(self.processor_status & 0b00001000) >> 3}\tI: {(self.processor_status & 0b00000100) >> 2}\tZ: {(self.processor_status & 0b00000010) >> 1}\tC: {(self.processor_status & 0b00000001)}\t")
        print("--------------------------------------")
