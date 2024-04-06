
from datetime import datetime
from functools import wraps

def debugger_decorator(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.debug:
            formatted_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            result = func(self, *args, **kwargs)
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

            return result
        else:
            return func(self, *args, **kwargs)

    return wrapper

