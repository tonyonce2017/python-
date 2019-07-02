area = {
        "广东":{
            "深圳":["罗湖区","南山区","龙岗区","福田区"], 
            "广州":["萝岗区","海珠区","荔湾区"]
        },
        "湖南":{
            "长沙":["芙蓉区","雨湖区"],
            "株洲":["天元区","石峰区"]
        }
}
print("请按照提示选择省/市/区, 'r'返回上一级.")
while True:
    sheng = input("选择省份[{0}]:".format("|".join(list(area.keys()))))
    if sheng == "r":
        print("没有上一级啦!")
    elif sheng in area.keys():
        _shi = area[sheng]
        while True:
            shi = input("选择{0}的城市[{1}]:".format(sheng,"|".join(list(_shi.keys()))))
            if shi == "r":
                break
            elif shi in _shi.keys():
                _qu = area[sheng][shi]
                while True:
                    qu = input("城市{0}的区[{1}], 请返回上级:".format(shi, "|".join(_qu)))
                    if qu == "r":
                        break
                    else:
                        print("输入有误!")
            else:
                print("输入有误!")
    else:
        print("输入有误!")
        
                    
                


