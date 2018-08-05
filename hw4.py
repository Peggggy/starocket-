# file=open("test.txt",mode="w")
# file.write("妳好嗎?\n好棒棒")
# file.close()

# with open("test.txt", mode="w") as file:
#     file.write("5\n4\n3\n2\n1")

# sum=0
# with open("test.txt", mode= "r") as file:
#     for line in file:
#         sum+=int(line)
# print(sum)

import urllib.request as request
import json
src= "http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=36847f3f-deff-4183-a5bb-800737591de5"
with request.urlopen(src) as response:
    data=json.load(response)
keyword=input("搜尋捷運站：")
list=data["result"]["results"]

with open("taipeifun.txt", "w", encoding = "utf-8") as file:
    for trans in list:
        if keyword == trans["MRT"]:
            print(trans["stitle"],trans["MEMO_TIME"])
            file.write(trans["stitle"] + "\n")
            # file.write("\n")