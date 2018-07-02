# n1 = int(input("Enter a number:"))
# n2 = int(input("Enter a number:"))
# op = input("加減乘除:")

# if op == "+":
#     print(n1+n2)
# elif op == "-":
#     print(n1-n2)
# elif op == "*":
#     print(n1*n2)
# else:
#     print(n1/n2)


n=int(input("輸入一個正整數"))
answer = 1
while answer < n:
    if answer*answer == n:
        print(answer)
        break
    answer+=1
if answer == n:
    print("no")

# for n in range(1,10):
