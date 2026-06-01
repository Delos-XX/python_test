height = float(input("请输入身高（米）: "))
weight = float(input("请输入体重（千克）: "))

bmi = weight / (height * height)

print("你的 BMI 是: %.2f" % bmi)

if bmi < 18.5:
    print("评价: 偏瘦")
elif bmi < 24:
    print("评价: 正常")
elif bmi < 28:
    print("评价: 超重")
else:
    print("评价: 肥胖")
