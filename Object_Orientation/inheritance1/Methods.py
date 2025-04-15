class Student:
    def cook(self):
        print('Student is cooking')
    def play(self):
        print('Playing cricket')

class Employee:
    def work(self):
        print('Employee is working')
    def cook(self):
        print('Employee is cooking')

e = Employee()
e.play()

'''
work():Specialised Method: Present only in chid class
play():Inherited Method: Used as it is in child class
cook():Overridden Method: Change implementation in child
'''