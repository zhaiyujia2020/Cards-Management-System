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
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入qq：")
    email_str = input("请输入邮件：")
    # 2.使用用户输入信息建立一个名片字典
    card_dic = {"name": name_str,
                "phone": phone_str,
                "qq": qq_str,
                "email": email_str
                }
    # 3.将名片字典添加到名片列表中
    card_list.append(card_dic)
    # 4.提示用户添加成功
    print("-" * 50)
    print(card_list)
    print("-" * 50)
    print("%s的名片新建成功" % name_str)
    print("-" * 50)


def show_all():
    """显示全部"""
    print("-" * 50)
    # 1.未查询到结果，对用户进行提示
    if len(card_list) == 0:
        print("未查询到结果")
        print("-" * 50)
        return
    # 2.查询到结果，以类似列表形式整齐漂亮的打印出全部名片内容
    print("显示全部名片")
    print("-" * 50)
    # 打印表头
    for card_list_title in ["姓名", "电话", "QQ", "邮件"]:
        print(card_list_title, end="\t\t")
    print("")
    # 遍历名片列表依次输出字典信息
    for card_dic in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dic["name"], card_dic["phone"], card_dic["qq"], card_dic["email"]))
    print("-" * 50)

def search_card():
    """查询名片"""
    print("-" * 50)
    print("查询名片")
