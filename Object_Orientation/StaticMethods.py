class MathOperations:
    @staticmethod
    def add_numbers(a, b):
        return a + b
    
result = MathOperations.add_numbers(5, 3)
print(result)

math_op = MathOperations()
print(math_op.add_numbers(10, 5))