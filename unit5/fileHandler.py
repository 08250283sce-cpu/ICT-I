greetings=open("hello.txt","r")
print(greetings)
greetings.close()
f=open("hello.txt","r")
print("filename:",f.name)
print("file mode:",f.mode)
print("Is file closed?",f.closed)
f.close()
print("Is file closed?",f.closed)
f=open("hello.txt","r")
contents=f.read()
print(contents)
f.close()

#writing a file 
newfile=open("newfile.txt","w")
print(newfile)
newfile.write("This is a new file created by python")
newfile.close()

#filwe overwrite
fileoverwrite=open("newfile.txt","w")
fileoverwrite.write("the contents of the new file is now changed.")
fileoverwrite.close()

#append a file 
appendfile=open("hello.txt","a")
appendfile.write("\n\nDon't foget to smile today!")
appendfile.close()

#with satement 
with open("hello.txt","r")as f:
    contents=f.read()
    print(contents)