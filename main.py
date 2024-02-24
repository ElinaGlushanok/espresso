from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QApplication
import sqlite3
import sys

class coffee(QMainWindow):
    def __init__(self, table):
        super().__init__()
        uic.loadUi('coffee.ui', self)
        try:
            self.tableWidget.setRowCount(len(table))
            self.tableWidget.setColumnCount(len(table[0]))
            for i, elem in enumerate(table):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        except IndexError:
            print('таблица пока что пустая')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    conn = sqlite3.connect('coffee.sqlite')
    cur = conn.cursor()
    data_table = cur.execute(f"SELECT * FROM Data").fetchall()
    window = coffee(data_table)
    window.show()
    sys.exit(app.exec_())