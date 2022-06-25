# 数字阶乘如输入6，输出6*5*4*3*2*1的结果

def jiecheng(num):
    zongshu = 1
    while num>0:
        zongshu*=num
        num-=1
    return zongshu

print(jiecheng(6))