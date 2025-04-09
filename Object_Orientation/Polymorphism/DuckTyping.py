class Add:
    def calculate(self, a, b):
        print('Addition:',a+b)

class Sub:
    def calculate(self, a, b):
        print('Subtraction:',a-b)

class Mul:
    pass

def permit(ref, a, b):
    if type(ref).__name__ == 'Mul':
        print('Mul class does not have calculate()')
    else:
        ref.calculate(a,b)
permit(Add(),10,20)
permit(Sub(),20,10)
permit(Mul(),10,20)
"""ref wont check the type of object.
ref only gives importance to the calculate method.
ref only gives importance to the methods of object."""