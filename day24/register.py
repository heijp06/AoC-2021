from __future__ import annotations
from expressions import InputExpression, BinaryExpression, ValueExpression
import operator
import math


class Register:
    BinaryOperations = {
        "mul": (operator.mul, '*'),
        "add": (operator.add, '+'),
        "mod": (operator.mod, '%'),
        "div": (lambda v1, v2: math.trunc(v1 / v2), '/'),
        "eql": (lambda a, b: 1 if a == b else 0, '==')
    }

    def __init__(self) -> None:
        self.values = {0}
        self.expression = ValueExpression(0)

    def __repr__(self) -> str:
        return repr((self.values, self.expression))
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Register) and self.values == other.values and self.expression == other.expression

    def inp(self, name: str) -> None:
        self.values = set(range(1, 10))
        self.expression = InputExpression(name)

    def binary_operation(self, operation: str, right: int | Register) -> None:
        func, symbol = Register.BinaryOperations[operation]
        if isinstance(right, int):
            right_values = {right}
            right_expression = ValueExpression(right)
        else:
            right_values = right.values
            right_expression = right.expression

        values = {
            func(v1, v2)
            for v1 in self.values
            for v2 in right_values
        }

        if values == self.values:
            return
        
        if values == right_values:
            self.values = right_values
            self.expression = right_expression
            return

        self.values = values
        if len(values) == 1:
            self.expression = ValueExpression(list(values)[0])
        else:
            self.expression = BinaryExpression(symbol, self.expression, right_expression)
        return
