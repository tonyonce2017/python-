import json

with open("acount.json", "r") as f:
    acounts = json.load(f)
    f.close

count = 0
while count < 3:
    name = input("请输入用户名: ")
    passwd = input("请输入密码: ")

    if name in acounts.keys():
        # 判断是否锁定
        if acounts[name]["useable"] == "false":
            print("您的账户已被锁定, 请联系系统管理员!")
            break
        if acounts[name]["passwd"] == passwd:
            print("登录成功, 欢迎%s使用!" % name)
            break
        else:
            print("密码错误, 你还有{0}次机会!".format(2-count))
            count += 1
    else:
        print("账户不存在!")
        count = 0
else:
    print("连续输错3次, 账户已锁定!")
    acounts[name]["useable"] = "false"
    with open("acount.json","w") as f:
        json.dump(acounts, f)
    

