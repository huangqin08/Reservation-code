import random
import time

# 预约项目编号
number = '78'

# 条线名称
stripline_name = '工行条线'

# 时间
now = time.strftime('%Y-%m-%d')

# 预约编码规则，首字母
initial = 'CFCCDE'

# 预约编码个数
num = 10

filename = number + stripline_name + '-' + '预约编码' + now + '.xls'
print(filename)

# filepath = '../Codefiles/' + filename

filepath = 'D:\\PythonProject\\ReservationCode\\Codefiles\\' + filename

# fp = open(filepath, wb)
print(filepath)
with open(filepath, 'w', encoding='UTF-8') as fw:
    for i in range(num):
        result = str(random.randint(0, 99999999)).zfill(8)
        code = initial + result
        fw.write(code)
        print(result)


