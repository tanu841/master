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