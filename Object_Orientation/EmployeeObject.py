class Employee:
    company_name = 'code' #Class Based variable
    def __init__(self, name, age, designation):
        self.name = name
        self.age = age
        self.designation = designation

    def login(self, time):
        print(f"{self.name} logged in at {time}Am")

    def logout(self, time):
        print(f"{self.name}, loggedout at {time}Pm")

    def work(self, hours):
        print(f'{self.name} worked for {hours}')

    def getDetails(self):
        print('Employee Name:',self.name)
        print('Employee Age:',self.age)
        print('Employee Designation:',self.designation)

e1 = Employee('Nethaji', 22, 'Developer')
e2 = Employee('Pooja', 23, 'Manager')
e3 = Employee('Rani', 26, 'SDE')

e1.getDetails()
e2.getDetails()
e3.getDetails()

