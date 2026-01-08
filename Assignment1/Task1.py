num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

add = num1=num2
sub=num1-num2
multiply=num1*num2

if num2 !=0:
    divide=num1/num2
else:
    divide="not divisible"
    
print("Addition:",add)
print("Subtraction:",sub)
print("multiply:",multiply)
print("division:",divide)