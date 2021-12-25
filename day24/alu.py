import re
from register import Register


class Alu:
    def __init__(self) -> None:
        self.w = Register()
        self.x = Register()
        self.y = Register()
        self.z = Register()

    def __repr__(self) -> str:
        return repr((self.w, self.x, self.y, self.z))
    
    def parse(self, rows: list[str]) -> None:
        input_ordinal = ord('A')
        for count, row in enumerate(rows):
            print(count, row)
            instruction, register_name, *arguments = row.split()
            register = self.register(register_name)
            if instruction == "inp":
                register.inp(chr(input_ordinal))
                input_ordinal += 1
            else:
                if re.search(r"\d", arguments[0]):
                    argument = int(arguments[0])
                else:
                    argument = self.register(arguments[0])
                register.binary_operation(instruction, argument)
            print(self)
            input()

    def register(self, name: str) -> Register:
        return getattr(self, name)
