# d = ""
# ip_list=[18,127,235,99]
# for i in ip_list:
#     a = bin(i).replace('0b','')
#     if len(a) < 8:
#         b = 8 - len(a)
#         a = b * "0" + a
#     d += a
# print(d)

# b = 0
# for i in range(len(d)):
#     b += 1
# print(b)

# a = '1,2,3'
# b = a.split()
# print(b)

# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]

# li.append("serven")
# print(li)
# li.insert(0,"Yony")
# print(li)
# l2=[1,"a",3,4,"heart"]
# for i in l2:
#     li.append(i)
# print(li)
# li.remove("ritian")
# print(li)
# li.pop(1)
# print(li)

# users = ["武沛齐","景女神","肖大侠"]
# for i in range(len(users)):
#     print(f'{i+1} {users[i]}')

# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis[2]="K"
# print(lis)

# lis[lis.index(3)]="100"
# print(lis)

# lis[3][2][1][0] = 101
# print(lis)

# lis[3].insert(0,"火车头")
# print(lis)

# googs = ['汽车','飞机','火箭']
#
# for i in range(len(googs)):
#     print(f'{i+1},{googs[i]}')
#
# choose = int(input("输入你想买的物品:"))
# print(googs[choose-1])

# lis = []
# li = ["wupeiqi ", "alexC", "AbC ", "seven", " riTiAn", "WuSir", "  aqc"]
# for i in li:
#     a = i.strip()
#     if a.startswith("a"):
#         lis.append(a)
#
# for i in lis:
#     print(i)

# li = ["alex",[11,22,(88,99,100,),33],"WuSir", ("alex", "barry",), "eric"]
# tup = (87,99,100,)
#
# li[1][2] = tup
# print(li)

# users = ['李少奇','李启航','渣渣辉']
# b = "_".join(users)
# print(b)

# v1 = (11,22,33,44,55,66,77,88,99)
# v2 = [44,55,66]
# for i in range(len(v1)):
#     if i != 0:
#       if i % 2 == 0:
#           v2.append(v1[i])
# print(v2)


l = ['a','a']
l.remove('a')
print(l)