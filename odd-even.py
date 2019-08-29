num1=0
num2=-1
sum_even=0
sum_square_odd=0
while num1>num2:
	num1 = int(input("Enter the first number:	"))
	num2 = int(input("Enter the second number(must be greater than first number):	"))
	if num1>num2:
		print("Oops, try again")
while num1<=num2:
	if (num1 % 2) != 0:
		print(num1,end=",")
		sum_square_odd=sum_square_odd+(num1*num1)
	else:
		sum_even=sum_even+num1
	num1=num1+1
print()
print(sum_even)
print(sum_square_odd)
