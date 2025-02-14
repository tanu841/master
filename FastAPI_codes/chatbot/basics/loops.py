my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(my_list)
x=0
while x<len(my_list):
    for x in range(0,len(my_list)):
        if my_list[x]=="Monday":
           continue
        else:
            print(my_list[x])
            x+=1