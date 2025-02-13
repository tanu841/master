my_List=[80,96,72,100,8]
print(my_List)
print(my_List[3])
print(my_List[1:4])
print(my_List[2:])
print(my_List[:3])
print(my_List[-1])
print(my_List[-3])
print(my_List[-4:-1])
# print(my_List[5]) error as 5th position is not there

people_list=["Eric","John","Michael","Terry","Graham","TerryG","Brian"]
print(people_list)
print(people_list[0]=="Erica") #False as the 0th position is eric not erica
people_list[0]="Erica"
print(people_list)