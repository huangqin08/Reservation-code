import random
import time
import xlsxwriter
import configparser


def code_do(filepath, num, initial):
    workfile = xlsxwriter.Workbook(filepath)  # 创建Excel文件,保存
    worksheet = workfile.add_worksheet('预约编码')  # 创建工作表
    col = ['A1']
    title = ['预约编码']
    worksheet.write_row(col[0], title)

    for i in range(num):
        result = str(random.randint(0, 999999)).zfill(6)
        code = initial + result
        worksheet.write(i + 1, 0, code)
        print(result)
    workfile.close()
    return filepath


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config_path = '../Config/co_config.conf'
    config.read(config_path, encoding='utf-8')
    # sec=config.sections()
    # op = config.options("code_project")
    # config.items("code_project")
    number = config.get('code_project', 'number')
    stripling_name = config.get('code_project', 'stripling_name')
    initial = config.get('code_project', 'initial')
    num = config.getint('code_project', 'num')

    # 文件名称中的时间
    now = time.strftime('%Y-%m-%d')
    filename = number + stripling_name + '-' + '预约编码' + now + '.xls'
    filepath = 'D:\\PythonProject\\ReservationCode\\Codefiles\\' + filename
    code_do(filepath, num, initial)
