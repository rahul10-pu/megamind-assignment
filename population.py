p_a = int(input("What is the population of town A? "))
g_a = int(input("What is the growth rate of town A? "))
p_b = int(input("What is the population of town B? "))
g_b = int(input("What is the growth rate of town B? "))
print("******************************************")
counter=0
if p_a>p_b:
	print("The population of town A is already the same or larger than town B.")
while p_a<p_b:
	p_a=p_a+((g_a/100)*p_a)
	p_b=p_b+((g_b/100)*p_b)
	counter=counter+1
	print("year:"+str(counter)+" | town A: "+str(p_a)+" | town B: "+str(p_b))

print("Number of years:"+str(counter))
print("******************************************")