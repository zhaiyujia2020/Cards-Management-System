# 获取用户输入的操作选项
option_num = int(input("请输入您想执行操作的序号："))
print("您选择的操作是【%d】" % option_num)

# 输入1、2、3，执行相应的名片操作
if option_num in [1, 2, 3]:
    pass
# 输入0，退出名片系统
elif option_num == 0:
    pass
# 输入其他内容，提示用户输入错误
else:
    print("你输入的不正确，请重新选择")