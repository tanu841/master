details ={}



def trial_name(firstname, lastname, age) :
        details["firstname"]=firstname
        details["lastname"]=lastname
        details["age"]=age
        return details


firstname_1=input("Enter your first name: ")
lastname_1=input("Enter your last name: ")
age_1=input("Enter your age: ")
trial_name(firstname_1,lastname_1,age_1)
print(details)