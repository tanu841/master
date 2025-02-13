myset ={1,2,3,4,5,1,2}
print(myset) #set removes duplicates in lent=gth as well
print(len(myset))

for x in myset:
    print(x)

myset.discard(3)
print(myset)
myset.add(6)
print(myset)
myset.update([7,8])
print(myset)
myset.remove(2)
print(myset)


#Tuple unchangable no addition
mytuple =(1,2,3,4,5)
print(mytuple)
print(mytuple[2])
print(len(mytuple))
# mytuple.add this functionality doesn't exists

