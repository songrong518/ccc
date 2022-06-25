# 编写一个程序，提示用户输入其名字和年龄；用户作出响应后，将其名字和年龄写
# 入到文件xxx.txt 中。
# 每个用户一行，【名字,年龄】
# 当输入的是”退出”的时候，退出输入，否则继续输入新的名字和年龄

with open("..//name.txt", "w+") as file:
    while True:

        name = input("请输入您的姓名：")
        age = input("请输入您的年两：")

        if name == "q" or age == "q":
            break
        else:

            file.writelines(f"{name},{age}\n")
