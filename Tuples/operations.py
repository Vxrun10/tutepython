# concatination

t1=(1,2,3,4)
t2=(7,6,5,4)

print(t1+t2)

#count

t3=(10,20,30,30,10,50,20,70)
print(t2)
print(f"Select the no from the above tuple")
item_count= int(input("Enter The Number: "))
c=t2.count(item_count)
print(f"The no of time {item_count} is {c}")

# min/max

t4=(10,20,100,33.5)
print(f"The minimum no in the tuple is {min(t4)}")
print(f"The maximum no in the tuple is {max(t4)}")

# in / not in()

t5=(101,"varun",2,"Hitti")

print(101 in t5)
print(101  not in t5)


# index():- Tells the index of an element

t6=(12,45,67)
print(t6.index(67))



