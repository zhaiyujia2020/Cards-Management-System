# 无限循环，由用户主动决定什么时候退出循环！
while True:
    # TODO（翟羽佳） 显示功能菜单

    # 获取用户输入的操作选项
    option_num = int(input("请输入您想执行操作的序号："))
    print("您选择的操作是【%d】" % option_num)

    # 输入1、2、3，执行相应的名片操作
    if option_num in [1, 2, 3]:
        # TODO(翟羽佳) 1：新建名片
        if option_num == 1:
            pass
        # TODO（翟羽佳） 2：显示全部
        elif option_num == 2:
            pass
        # TODO（翟羽佳） 3：查询名片
        elif option_num == 3:
            pass
    # 输入0，退出名片系统
    elif option_num == 0:
        print("欢迎再次使用【名片管理系统】")
        break
    # 输入其他内容，提示用户输入错误
    else:
        print("你输入的不正确，请重新选择")