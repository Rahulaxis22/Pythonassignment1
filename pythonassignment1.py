# Assignment: Take multiple numbers through input and print the sum of the numbers.
num=input("Enter the numners")
num2=num.split()
sum=0
for i in num2:
     sum+=int(i)
print(sum)
