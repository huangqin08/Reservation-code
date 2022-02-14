from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from Code.PQ_openpyxl_createcode import code_do
class Stats:
    def __init__(self):
        self.ui = QUiLoader().load('createCode.ui')
        self.ui.pushButton.clicked.connect(self.createcode)

    def createcode(self):
        number = self.ui.number_lineEdit.text()
        stripling_name = self.ui.stripling_name_lineEdit.text()
        initial = self.ui.lineEdit_initial.text()
        num = int(self.ui.lineEdit_num.text())
        specification = self.ui.lineEdit_specification.text()
        product_name = self.ui.lineEdit_product.text()
        channel = self.ui.lineEdit_channel.text()
        code_do(number, stripling_name, initial, num, specification, product_name, channel)


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
