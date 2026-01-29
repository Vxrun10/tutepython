#Slicing of list
list1=[1,2,3,4,5,6,7,8]
print(list1[1:7:1])

# concatination of list

list2=[1,2,8]
print(list1+list2)

# repetation of list
list3=[1,2,8]
print(list3)

# Append Function:- It add any Element at the end of the list,it can add only 1 element at a time
# insert function:- Add any Element at the desired index

l1=["Mango","Banana","Coconut"]
print(l1)
l1.insert(1,"Kiwi")
l1.append("Apple")
print(l1)

#  Extend Functin:- It can add elemnt more than 1 in  a list
list4=["Varun","Hitarth","Tanish","Ojasvi"]
list4.extend(["Kannu","Lucky"])
print(list4)
print(f"The len of the list is",len(list4))
print(f"The no 2 element in the list is {list4[1]}")

#remove function 
list5=["Varun","Hitarth","Tanish","Ojasvi"]
print(list5)
list5.remove("Ojasvi")
print(list5)

# pop function:- it takes 'INDEX 'to remove the element
list6=["Varun","Hitarth","Tanish","Ojasvi"]
list6.pop(2)
print(list6)

# Reverse Function
list7=[4,6,8,9,0,1,2]
print(list7)
list7.reverse()
print(list7)

#Sort Fundtion

list8=[9,7,8,6,3,1,0]
print(list8)
list8.sort()
print("The sorted list is in ascending oreder:- ",list8)

list8.sort(reverse=True)
print("The list is sorted in descending order:-",list8)

# Count Function

list9=[1,2,4,3,2,1,6,1]
print(f"Select the number from this list {list9}")
Item_to_count=int(input("Enter The Number:-"))
c=list9.count(Item_to_count)
print(f"The no appearence {Item_to_count} is ",c)

#Membership operation
#(in)
list10=["python","java","javascript","flask"]
print("python" in list10)
#(not in)
print("python" not in list10)
print("seaborn" not in list10)

