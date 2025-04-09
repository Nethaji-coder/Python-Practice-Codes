class Demo1:
    def __init__(self, name):
        self.__name = name #Private Variable

d1 = Demo1('Akash')
#print(d1.__name) #Error
print(d1._Demo1__name) #Akash

'''
1.NameMangling is the process of providing new name 
to the private variables.

2.These new names will be provided automaticall by 
python for all private members.

3.New Name will be provided in format:
objectName._className__VariableName

'''
