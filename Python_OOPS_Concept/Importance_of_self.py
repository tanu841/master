#Understanging the requirement oif self parameter in pythin 
class Employee:
    def employeeDetails():
        pass
employee=Employee()
employee.employeeDetails()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-6b55ea920b88> in <module>
      1 employee=Employee()
----> 2 employee.employeeDetails()

TypeError: employeeDetails() takes 0 positional arguments but 1 was given

#note- error is thrown abnbove becausr py calls employee.employeeDetails() as Employee.employeeDetails(employee), as  a result the obj is always sent as a paramenter to rectify it we use self, anything welse can also be used but self is agenericc term to avoid any confusion
#correcting the above issue with self
class Employee:
    def employeeDetails(self):
        pass
employee=Employee()
employee.employeeDetails()
#successful 
class Employee:
    def employeeDetails(self):
        self.name='Matthew'
        print('Name: ',self.name)
        age =10
        print('Name: ',age) #why use self .attribute when using only attribute works 
        
employee=Employee()
employee.employeeDetails()
Name:  Matthew
Name:  10
#note- using self lets the attribute to be globally declared, such as below 
class Employee:
    def employeeDetails(self):
        self.name='Matthew'
        print('Name: ',self.name)
        age =10
        print('Name: ',age) #why use self .attribute when using only attribute works
    
    def printemployeedetaikls(self):
        print('Printing in another method' )
        print('Name: ',self.name)
        print('Name: ',age) #error as age is not globally declared 
        
employee=Employee()
employee.employeeDetails()
employee.printemployeedetaikls()
Name:  Matthew
Name:  10
Printing in another method
Name:  Matthew
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-8-b03b3faa9e96> in <module>
     14 employee=Employee()
     15 employee.employeeDetails()
---> 16 employee.printemployeedetaikls()

<ipython-input-8-b03b3faa9e96> in printemployeedetaikls(self)
     10         print('Printing in another method' )
     11         print('Name: ',self.name)
---> 12         print('Name: ',age) #error as age is not globally declared
     13 
     14 employee=Employee()

NameError: name 'age' is not defined
