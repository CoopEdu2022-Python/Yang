# 5.1.2 定义两个列表，分别存储平年和闰年的每个月份的天数，按照月份打印这个月的天数
# 例：平年的 1 月有 31 天，闰年的 1 月有 31 天
平年=[31,28,31,30,31,30,31,31,30,31,30,31]
闰年=[31,29,31,30,31,30,31,31,30,31,30,31]
for a in range(0,12):
    b=a+1
    print("平年%d月有%d天，闰年%d月有%d天"%(b,平年[a],b,闰年[a]))