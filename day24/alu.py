import math
import operator
import re


class ALU:
    def __init__(self, program: list[int]) -> None:
        self.program = program
        self.intialize()
        self.instructions = {
            "add": operator.add,
            "mul": operator.mul,
            "div": lambda a, b: math.trunc(a / b),
            "mod": operator.mod,
            "eql": lambda a, b: 1 if a == b else 0
        }

    def __repr__(self) -> str:
        return repr((self.x, self.y, self.z, self.z))

    def intialize(self) -> None:
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0

    def run(self, inputs: list[int]) -> None:
        self.intialize()
        index = 0
        for instruction in self.program:
            name, register, *rest = instruction.split()
            if rest:
                func = self.instructions[name]
                arg = int(rest[0]) if re.search(
                    r"\d", rest[0]) else self.get(rest[0])
                result = func(self.get(register), arg)
            else:
                result = inputs[index]
                index += 1
            self.set(register, result)

    def get(self, register: str) -> int:
        return getattr(self, register)

    def set(self, register: str, value: int):
        setattr(self, register, value)
