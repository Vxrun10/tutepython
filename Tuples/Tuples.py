#Tuple: It is a sequence of item as a collection,we cannot modify the ,These are immutable


t1=("Jnauray","Feburary","March",10,True,(10,20))
print(f" The length of the tuple is : {len(t1)}")
print(t1[0])
print(t1[-1])


#Typecasting of tuple into list
print(type(t1))
l2=list(t1)
print(l2,type(l2))


