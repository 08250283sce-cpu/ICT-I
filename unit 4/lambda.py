name=input("Enter your name:")
greet = lambda y:print("Hello",y)
greet(name)


# use case of lambda

even_odd=lambda x:"even" if x%2==0 else "odd"
num=int(input("enter a number:"))
print(even_odd(num))

arith= lambda x,y:(x+y,x-y,x*y,x/y)
num1= int (input("enter the first number"))
num2= int (input("enter the second number"))
print(arith(num1,num2))

#filter and lambda
my_list =[1,2,3,4,5,6,]
even = filter(lambda x: x%2==0, my_list)
print(list(even))

#map()
mylist = [1, 2, 3, 4]

double = list(map(lambda x: x*2, mylist))
print("Doubled:", double)  
original = list(map(lambda x: x//2, double))
print("Original:", original)  

# reduce()
from functools import reduce
mylist=[1,2,3,4]
mul =reduce(lambda x,y:x*y,mylist)
print(mul)

even_odd=lambda x:"even" if x%2==0 else "odd"
num=int(input("enter a number:"))
print(even_odd(num))


#excercise for lambda

num=int(input("enter the number:"))
check_num = lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Zero")
print(check_num(num))
