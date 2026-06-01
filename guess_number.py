import random

answer = random.randint(1, 100)
count = 0

print("猜数字游戏开始！")
print("系统已经生成了一个 1 到 100 之间的随机数。")

while True:
    guess = int(input("请输入你猜的数字: "))
    count = count + 1

    if guess > answer:
        print("猜大了")
    elif guess < answer:
        print("猜小了")
    else:
        print("恭喜你，猜对了！")
        print("你一共猜了 %d 次。" % count)
        break
