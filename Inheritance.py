class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showDetails(self):
        print(f"The name of the employee:{self.id} is {self.name}")

class Programmer(Employee):    #inheritance class
    def showLanguage(self):
        print("The default language is python")

e1=Employee("Rohan",400)
e1.showDetails()
e2=Employee("Harry",250)
e2.showDetails()
e2=Programmer("Harry",250)    #inheritance
e2.showDetails()
e2.showLanguage()