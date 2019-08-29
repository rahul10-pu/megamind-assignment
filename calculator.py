# This function adds two numbers 
def add(x, y):
   return x + y
# This function subtracts two numbers 
def subtract(x, y):
   return x - y
# This function multiplies two numbers
def multiply(x, y):
   return x * y
# This function divides two numbers
def divide(x, y):
	if y==0:
		return "Invalid denominator"
	return x / y
num1 = int(input())
num2 = int(input())
op = input()
if op == '+':
   print(num1,"+",num2,"=", add(num1,num2))
elif op == '-':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif op == '*':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif op == '/':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")