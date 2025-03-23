#WAP to display 'Child' if age is below 18, display 'Adult' if age is above 18,
#display senior Citizen if age is above 65.
def displayAge(age):
    if(age<18):
        print('Child')
    elif(age>18 & age<65):
        print('Adult')
    else:
        print('Senior Citizen')
displayAge(int(input('Enter your age')))
