# for i in range(1,11):
#     print(i)

# s1="hello world"

# for char in s1:
#     print(char)  
# print("End of the Loop")  

# employee={'empid':1001,'name':"varun",'city':"delhi"}
# for id in employee.items():
#     print(id[0],id[1])
#-------------------------------------

## range()- (start,stop,slice/steps)
## range()- (start,stop)== step 1 by default
## range()- (stop)== start by 0 and stop at the desired value 

# for i in range(10,0,-1):
#     print(i)
# print("Happy New Year!!!")

# for id in range(0,8):
#     print(id)

# for ide in range(7):
#     print(ide)

# gorceries=['salt','milk','sugar']
# for item in range(3):
#     print(item)

# profits=['9','3','12','10']
# for index in range(len(profits)):
#     q = index+1
#     print(f"The Quarter of index {q} is {profits[index]}")
#------------------------------------------------------

# min and max number
scores=['2','44','56','99','78','87','77']

total = 0
for score in scores:
    total = total + int (score)

print(f"The total of the team is {total}")

total =sum(int(score) for score in scores)
print(f"The total of the team is {total}")

###3
highest = scores[0]
for score in scores:
    if highest<score:
        highest=score
print(f"The highest score is {highest}")
# ------------------------------------------

max()/min
highest = max(scores) 
print(f"The highest score is:- {highest}")

lowest = min(scores) 
print(f"The lowest score is:- {lowest}") 

# ---------------------------------------------
# # WHILE LOOP







    
    