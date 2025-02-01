#Learnign about class attribute and instance attribute
class Employee:
    numberOfWorkingHours =40
#Declaring objects of class
employeeOne=Employee()
employeeTwo=Employee()
#calling the object1 
employeeOne.numberOfWorkingHours
#result of the object1 
40
#calling the object 2
employeeTwo.numberOfWorkingHours
#result of object 2
40
#creating an instance attribute only for obbj 1
employeeTwo.name='Mary'
employeeTwo.name
#result of instance attribute only for obbj 1
'Mary'
#result of instance attribute for obbj 2
employeeOne.name
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-7-1faee0f3f6f5> in <module>
----> 1 employeeOne.name

AttributeError: 'Employee' object has no attribute 'name'

#creating an instance attribute for working hours to overwrite class attribute
employeeOne.numberOfWorkingHours =10
employeeOne.numberOfWorkingHours
#result oif creating an instance attribute for working hours to overwrite class attribute for obj 1
10
employeeTwo.numberOfWorkingHours
#result oif creating an instance attribute for working hours to overwrite class attribute for obj 1
40
#note- pyhton checks insxtance attriobute forst if there are no instance attribute then it checks the class attribute and prints it 
