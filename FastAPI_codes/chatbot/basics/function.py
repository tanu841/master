details ={}

class naming_fun:

    def trial_name(self,firstname, lastname, age) :
        details["firstname"]=firstname
        details["lastname"]=lastname
        details["age"]=age
        return details


name_obj=naming_fun()
firstname_1=input("Enter your first name: ")
lastname_1=input("Enter your last name: ")
age_1=input("Enter your age: ")
name_obj.trial_name(firstname_1,lastname_1,age_1)
print(details)