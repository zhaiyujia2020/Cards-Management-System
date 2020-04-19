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
    print("-" * 50)
    # 1.提示用户输入要查询的名片姓名
    find_name = input("请输入您要查询的名片姓名：")
    # 2。遍历名片列表，搜索要查询的名片姓名，如果存在，打印相关信息，如果不存在，提示用户不存在
    for card_dic in card_list:
        if find_name == card_dic["name"]:
            # 打印表头
            print("-" * 50)
            for card_list_title in ["姓名", "电话", "QQ", "邮件"]:
                print(card_list_title, end="\t\t")
            print("")
            print("-" * 50)
            # 打印查询到的名片的相关信息
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dic["name"], card_dic["phone"], card_dic["qq"], card_dic["email"]))
            print("-" * 50)
            # 针对找到的名片执行修改删除操作
            deal_card(card_dic)
            break
    else:
        print("-" * 50)
        print("您要查询的%s用户不存在" % find_name)
        print("-" * 50)


def deal_card(card_dic):
    """处理查找到的名片

    :param card_dic:查找到的名片
    """
    # 对找到的名片执行修改删除操作
    search_option = input("请选择要执行的操作 [1]修改 [2]删除 [其他任意键]返回上级菜单：")
    if search_option == "1":
        # 对查询到的名片进行修改操作
        card_dic["name"] = input_card_info(card_dic["name"], "姓名[直接回车不修改]：")
        card_dic["phone"] = input_card_info(card_dic["phone"], "电话[直接回车不修改]：")
        card_dic["qq"] = input_card_info(card_dic["qq"], "qq[直接回车不修改]:")
        card_dic["email"] = input_card_info(card_dic["email"], "邮箱[直接回车不修改]：")
        print("对查询到的名片进行修改操作")
    elif search_option == "2":
        # 对查询到的名片进行删除操作
        card_list.remove(card_dic)
        print("删除名片成功！")


def input_card_info(dic_value, input_tips):
    """输入名片信息

    :param dic_value:名片字典中原有的值
    :param input_tips:输入的提示文字
    :return:如果用户有输入内容，返回输入内容；否则，返回名片字典中原有的值
    """
    # 1.获取用户输入内容
    result_str = input(input_tips)
    # 2.针对用户的输入进行判断，如果用户输入了，返回输入结果
    if len(result_str) > 0:
        return result_str
    # 3.如果用户没有输入，返回字典的中原有的值
    else:
        return dic_value

