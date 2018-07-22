# n1=input("Enter a number:")
# n2=input("Enter a number:")
# n1= int(n1)
# n2= int(n2)

def mul(n1, n2):
    for x in range(n1 ,n2+1):
        for y in range(n1, n2+1):
            print(x,"*", y,"=" , x*y)
    return

# mul(n1,n2)

# n1 = int(input("Enter a number:"))
# n2 = int(input("Enter a number:"))
op = input("加減乘除:")

def cal(n1, n2):
    if op == "+":
        print(n1+n2)
    elif op == "-":
        print(n1-n2)
    elif op == "*":
        print(n1*n2)
    else:
        print(n1/n2)
    return

# cal(n1, n2)