import sys
import csv
import mainwindow
import table
from PyQt5 import QtWidgets, QtCore, QtGui
import outcomeList


class MainWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_table)

    def show_table(self):
        t = TableDialog()
        filename = self.filename_line.text()
        expression = self.expression_line.text()
        #inverted_index = index.get_index(filename)
        #outcome_list = spaceVectorModel.outcome_list(expression, inverted_index)
        outcome_list = outcomeList.get_outcome_list(filename, expression)
        csv_file = open(filename)
        csv_reader = csv.reader(csv_file)
        total_row = len(outcome_list)  # list当中的文档个数
        t.tableWidget.setColumnCount(5)  # 设置这个表有五列
        t.tableWidget.setRowCount(total_row)
        csv_reader_list = [row for row in csv_reader]  # csv表格中的全部内容存放在csv_reader_list中，每一行的内容是一个list
        for row in range(total_row):   # 对于结果当中的每一个文档
            row_number = outcome_list[row]  # 文档的编号是row_number
            # row_content = csv_reader[row_number-1]
            row_content = csv_reader_list[row_number-1]   # /home/fr/Desktop/test.csv
            for col in range(5):
                t.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem((row_content[col])))
        # t.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("abc"))
        t.exec()


class TableDialog(QtWidgets.QDialog, table.Ui_Dialog):
    def __init__(self):
        super(TableDialog, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())