# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
import time
import design  # imports the generated design code


class MainApp(QtGui.QMainWindow, design.Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		self.removeFileBtn.clicked.connect(self.remove_file_from_list)


	def remove_file_from_list(self):
		item_index = self.fileListWidget.currentRow()
		print item_index
		if item_index != -1:
			print self.fileListWidget.currentItem().text()
			self.fileListWidget.takeItem(self.fileListWidget.currentRow()) 
			del self.filenameList[item_index]
			print self.filenameList

def main():
	app = QtGui.QApplication(sys.argv)
	app_obj = MainApp()
	app_obj.show()
	app.exec_()

if __name__ == '__main__':
    main()