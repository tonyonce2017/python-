_name = "lc"
_passwd = "123456"
count = 0
while count < 3:
    name = input("请输入用户名: ")
    passwd = input("请输入密码: ")
    if name == _name and passwd == _passwd:
        print("登录成功, 欢迎使用!")
        break
    else:
        print("用户名或密码错误, 你还有{1}次机会!".format(2-count))
        count += 1
else:
    print("连续输错3次, 账户已锁定!")

