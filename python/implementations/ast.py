class Expression:
    def __str__(self):
        raise NotImplementedError

    def eval(self, variables):
        raise NotImplementedError


class Value(Expression):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def eval(self, variables):
        return self.value

class Constant(Expression):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def eval(self, variables):
        return variables[self.name]

class Operation(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, variables):
        if variables is None:
            variables = {}
        return self.operator(self.left, self.right, variables)

    @staticmethod
    def operator(left, right):
        raise NotImplementedError 

class Times(Operation):
    def __str__(self):
        return f"({self.left} * {self.right})"

    @staticmethod
    def operator(left, right, variables):
        return left.eval(variables) * right.eval(variables)


class Plus(Operation):
    def __str__(self):
        return f"({self.left} + {self.right})"

    @staticmethod
    def operator(left, right, variables):
        return left.eval(variables) + right.eval(variables)

if __name__ == "__main__":
    operation = Times(Value(3), Plus(Constant("x"), Constant("y")))

    variables = {
        "x": 1,
        "y": 3,
    }

    print(f"{operation} = {operation.eval(variables)}")
