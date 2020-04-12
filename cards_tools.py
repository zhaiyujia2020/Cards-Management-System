# 记录所有名片字典的列表
card_list = []


def show_menu():
    """显示功能菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    """新建名片"""
    print("-" * 50)
    print("新建名片")
    # 1.提示用户输入名片的详细信息
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    qq = input("请输入qq：")
    email = input("请输入邮件：")
    # 2.使用用户输入信息建立一个名片字典
    card_dic = {"name": name,
                "phone": phone,
                "qq": qq,
                "email": email
                }
    # 3.将名片字典添加到名片列表中
    card_list.append(card_dic)
    # 4.提示用户添加成功
    print("-" * 50)
    print(card_list)
    print("-" * 50)
    print("%s的名片新建成功" % name)
    print("-" * 50)


def show_all():
    """显示全部"""
    print("-" * 50)
    print("显示全部")


def search_card():
    """查询名片"""
    print("-" * 50)
    print("查询名片")
