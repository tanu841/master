"""class employee:
    def employeeDetails(self):
        self.name= 'Mark'
    def displayEmployeedetails(self):
        print(self.name)

employee=employee()
employee.displayEmployeedetails()"""
#error - AttributeError: 'employee' object has no attribute 'name' IN Py if the name is declared in another def then while creating the obj it must be called as well to initiate ti get this extra work out use init()

"""class employee:
    def __init__(self):
        self.name= 'Mark'
    def displayEmployeedetails(self):
        print(self.name)
employee=employee()
employee.displayEmployeedetails()
#result - Mark
"""
class employee:
    def __init__(self,name):
        self.name= name
    def displayEmployeedetails(self):
        print(self.name)

employeeone=employee("Mrk")
employeetwo=employee("Matthew")
employeeone.displayEmployeedetails()
employeetwo.displayEmployeedetails()

#attribute - prop that further defines a class
#method - function with ia class which can access all the attributes and perform sprecific task
#class attribute - attribute that are shared by all the instances of a class. they are created wither as part of the class or classnam.attribute
#instance attribute - attribute that are specific to each instance of a class. they are created within the __init__ method using objhname.attribute name
#instance method - method that are specific to each instance of a class. they are created within the class using def methodname(self): syntax
#static method - method that are not specific to any instance of a class. they are created within the class using @staticmethod decorator
#self - a generic term used to refer to the instance of a class. it is used to access the attributes and methods of the class within the class itself
