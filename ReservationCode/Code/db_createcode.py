import random
import time
import xlsxwriter
import configparser

from Code.myabc_db import MyABC_db

sl = MyABC_db('../Config/db_config.conf', 'TESTDB')


def code_do(filepath, num, initial, specification, channels):
    workfile = xlsxwriter.Workbook(filepath)  # 创建Excel文件,保存
    worksheet = workfile.add_worksheet('预约编码')  # 创建工作表
    col = ['A1', 'B1', 'C1']
    title = ['渠道名称', '预约规格', '预约编码']
    worksheet.write_row(col[0], title)

    creattime = time.strftime('%Y-%m-%d %H:%M:%S')
    print('num', num)
    for i in range(num):
        result = str(random.randint(0, 999999)).zfill(6)
        code = initial + result
        re = sl.select_record_fetchone("select * from codenumber where code = '%s' " % code)
        # re = sl.select_record_fetchone("select * from codenumber where code = 'ZBDC59628020'")
        print('re:', re)
        if re is None:
            worksheet.write(i + 1, 0, channels)
            worksheet.write(i + 1, 1, specification)
            worksheet.write(i + 1, 2, code)
            sl.insert_record(
                "insert into codenumber(code,createtime)values ('{}','{}')".format(code, creattime))
            print(result)
        else:
            print('预约编码重复，不进入数据库和excel表格中')
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
    specification = config.get('code_project', 'specification')
    product_name = config.get('code_project', 'product_name')
    channel = config.get('code_project', 'channel')

    # 文件名称中的时间
    now = time.strftime('%Y-%m-%d')
    filename = number + stripling_name + '-' + '预约编码' + now + '.xlsx'
    filepath = 'D:\\PythonProject\\ReservationCode\\Codefiles\\' + filename
    channels = channel + '-' + stripling_name + '-' + product_name
    code_do(filepath, num, initial, specification, channels)
