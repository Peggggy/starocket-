# Tutorial:文法  Library Reference:查字典
# 流程控制
# if 判斷式
# money=int(input("多少錢?"))
# if money <=0:
#     print("請輸入大於 0 的數字")
# elif money <= 30000:
#     print("OK")
# else:
#     print("Too Much")

# n1=int(input("Enter a Number"))
# n2=int(input("Enter a Number"))
# op=input("運算：+, -, *, /")
# if op=

# 中央處理器 CPU 1GHz, 10億個指令/每秒

# 迴圈
# break
# n=1
# while n<=5:
#     # 如果布林值是True, 執行這個區塊的程式碼
#     print(n)
#     n+=1
#     if n==3:
#         break #立刻終止迴圈
# print("Final", n)

# continue
# n=1
# while n<=5:
#     # 如果布林值是True, 執行這個區塊的程式碼
#     n+=1
#     if n==3:
#         continue  #立刻進入下一個圈圈
#     print(n)
# print("Final", n)

# n=1
# while n<=5:
#     # 如果布林值是True, 執行這個區塊的程式碼
#     n+=1
#     if n%2==0: # 如果 n 是偶數
#         continue  #立刻進入下一個圈圈
#     print(n)
# print("Final", n)

# 1+2+3+....+50
# sum=0 #紀錄最後加總的結果
# n=1 # 在迴圈中追蹤1,2,3,4,...,50
# while n<=5:
#     print(n, sum)
#     sum=sum+n # 將 n 的數字累加進 sum 裡面
#     n+=1
# print(sum)

# 作業
# n=int(input("輸入一個正整數"))
# 算整數平方根 9=>3, 25=>5, 8=>沒有
# 8
# 1, 2, 3, 4, 5, 6, 7

# for 變數名稱 in 列表:
#     迴圈區塊

for n in [2,5,6,7]:
    print(n)
print("======")
for x in range(1,6): # range(1,6)產生 [1,2,3,4,5]的列表
    print(x)