#creating class
class Employee:
    name="Ben"
    designation="Sales Executive"
    salesMadeThisWeek=6
    def hasAchievedTarget(self):
        if self.salesMadeThisWeek>=5:
            print("Target has been achieved")
        else:
            print("Target has not been achieved")
    
#creating object of the class
employee = Employee()
#call name of the employee
employee.name
'Ben'
#call the target achived if clause
employee.hasAchievedTarget()
​
Target has been achieved
numbers=[1,2,3]
type(numbers)
list
numbers.append(4)
numbers
[1, 2, 3, 4]
