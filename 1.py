#
# 给你一个由若干 0 和 1 组成的字符串s，请你计算并返回将该字符串分割成两个子字符串（即左子字符串和右子字符串, 子字符串允许为空）所能获得的最大得分。
# 已知分割字符串的得分规则如下：
# 左子字符串中：0得2分，1得1分
# 右子字符串中：1得2分，0得1分 
# 子字符串为空则得0分
# 输入描述:

#计算取值
def return_value(order,word):
    if order == "left":
        if word == "0":
            return 2
        elif word == "1":
            return 1
    elif order == "right":
        if word == "0":
            return 1
        elif word == "1":
            return 2
def main():
    test_str = "011101101010"#8位测试字符
    index = 0
    max_value = 0
    right_all_value = 0
    left_all_value = 0
    while(index < len(test_str)):
        right_value = 0  # 存储左右两值
        left_value = 0
        #利用字符串切片 取值
        left_str = test_str[0:index]
        right_str = test_str[index:]
        if index == 0:#左侧str留空
            left_str = ""
            right_str = test_str
        elif index == (len(test_str)-1):#右侧str留空
            left_str = test_str
            right_str = ""
        for r in list(right_str):
            right_value += return_value("right",r)
        for l in list(left_str):
            left_value += return_value("left",l)
        str_value = right_value + left_value
        print(f"left:{left_str} right:{right_str} left_len:{len(left_str)} right_len:{len(right_str)} left_value:{left_value} right_value:{right_value} str_value:{str_value}")

        if max_value < str_value:
            max_value = str_value
        index += 1
    print(f"MAX_VALUE:{max_value}")
if __name__ == '__main__':
    main();

