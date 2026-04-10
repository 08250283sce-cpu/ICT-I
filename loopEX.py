name= input("Enter your name:")
for i in name:
    print(i)
li = [ "Python Programming","Python Fundamentals","Python Interview Question"]
for x in li:
    print(x)    
lenli = len(li)
for x in range (lenli):
    print(li[x])

tup=tuple(li)
for x in tup:
    print(x)   
lentup = len(tup)
for x in range (lentup):
    print(tup[x])

my_set = set(li)
for x in my_set:
    print(x)   


