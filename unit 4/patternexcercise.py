
def sign(n):
    
    if n == 1:
        print("*")
        return
    else:
        
        sign(n - 1)
        
        print("* " * n)

sign(4)
