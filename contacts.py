contacts = {}

while True:
    print("")
    print("通讯录小程序")
    print("1. 添加联系人")
    print("2. 查找联系人")
    print("3. 删除联系人")
    print("4. 查看所有联系人")
    print("5. 退出")

    choice = input("请输入选项: ")

    if choice == "1":
        name = input("请输入姓名: ")
        phone = input("请输入电话: ")
        contacts[name] = phone
        print("添加成功")

    elif choice == "2":
        name = input("请输入要查找的姓名: ")
        if name in contacts:
            print(name + " 的电话是: " + contacts[name])
        else:
            print("没有找到这个联系人")

    elif choice == "3":
        name = input("请输入要删除的姓名: ")
        if name in contacts:
            del contacts[name]
            print("删除成功")
        else:
            print("没有找到这个联系人")

    elif choice == "4":
        if len(contacts) == 0:
            print("通讯录为空")
        else:
            for name in contacts:
                print(name + ": " + contacts[name])

    elif choice == "5":
        print("程序结束")
        break

    else:
        print("输入错误，请重新选择")
