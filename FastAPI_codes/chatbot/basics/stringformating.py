name="Blacck"
print("Hi " + name)
print(f"Hi {name}")
print("Hi {name}")
sentence="Hello {}"
print(sentence.format(name))

sentence="Hello {} {}"
lastname="Heart"
print(sentence.format(name,lastname))
"""
onename=input("Enter name: ")
days=input("Enter days: ")
print(f"Hi {onename} you have been here "
      f"for {days} days")
"""
#Assignmnent
days = int(input("How many days until your birthday:"))
week=round(days/7 ,2)
print(f"{week} weeks until your birthday")