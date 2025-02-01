class Employee:
    def employeeDetails(self):
        self.name='Ben'
    @staticmethod
    def welcomeMessage():
        print("If you want to run an def without self then make it statin method with @")
        #static method runs with out self
employee = Employee()
employee.employeeDetails()
print(employee.name) #Ben
employee.welcomeMessage()
