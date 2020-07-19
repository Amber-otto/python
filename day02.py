# for i in range(3):
#     num = int(input("请输入数字："))
#     if num >66:
#         print("猜大了")
#     elif num == 66:
#         print("恭喜你，正确")
#         break
#     elif num < 66:
#         print("猜小了")
#     if i == 2:
#         print("垃圾")

# num = 0
# for i in range(1,101):
#     num += i
# print(num)

# num = 0
# for i in range(1,100):
#     if i % 2 == 1:
#         num +=i
#     elif i % 2 ==0:
#         num -=i
# print(num)

# usern = "alex"
# passwd = "123456"
# print("您有三次机会重试")

# for i in range(2,-1,-1):
#     username = input("输入用户名:")
#     password = input("输入密码:")
#     if username == usern and password == passwd:
#         print("登陆成功")
#     elif username != usern or password != passwd:
#         print("登陆失败") 
#         print("剩余{0}次机会".format(i))  

#8bit = 1btye

#ascii 256 位 表示不了中文
# unicode 可以表示中文
# utf-8  压缩的unicode

# print(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)

# print(8 or 3 and 4 or 2 and 0 or 9 and 7)
# print(0 or 2 and 3 and 4 or 6 and 0 or 3)
# print(0 or 4 or 0 or 3)

# print(6 or 2 > 1)
# print(3 or 2 > 1)
# print(0 or 5 < 4)

# name = "aleXleNb"
# print(name[0:2])
# print(name[0:3])
# print(name[-2:])

# s = "123a4b5c"
# a = s[0:3]
# b = s[3:6]
# c = s[-1]
# d = s[-3::-2]
# print(d)

# i = 0
# s="asdfer"
# while i < len(s):
#     print(s[i])
#     i+=1

# s="321"
# a=len(s)
# while a > 0:
#     print("倒计时{0}秒".format(a))
#     if a == 1:
#         print("出发")
#     a -= 1   

# content = "fhdal234slfH9H769fjdla"
# num = 0 
# bum = 0
# for i in content:
#     if i == "h":
#         num += 1
#     elif i == "H":
#         bum += 1
# print(num)
# print(bum)

#message = "伤情最是晚凉天，憔悴厮人不堪言。"

# num = 0
# a = len(message)
# while a > 0:
#     print(message[a-1])
#     a -= 1
#i = 0
#a = len(message)
#while i < a:
#    print(message[i])
#    i += 1

