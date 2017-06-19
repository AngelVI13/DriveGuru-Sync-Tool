# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
import time
import design  # imports the generated design code
from drive_api import *
import os


class InfoPopup(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		
		self.setWindowTitle("Info")

		infoImgLabel = QtGui.QLabel("Test")

		okBtn = QtGui.QPushButton("OK")
		okBtn.clicked.connect(self.close_popup)

		layout = QtGui.QVBoxLayout()
		layout.addWidget(infoImgLabel)
		layout.addWidget(okBtn)
		self.setLayout(layout)


	def close_popup(self):
		self.emit(QtCore.SIGNAL('close_popup()'))


class MainApp(QtGui.QMainWindow, design.Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		self.uploadBtn.clicked.connect(self.single_upload)
		self.removeFileBtn.clicked.connect(self.remove_file_from_list)
		self.clearListBtn.clicked.connect(self.clear_file_list)
		self.selectFilesBtn.clicked.connect(self.select_files)
		self.infoBtn.clicked.connect(self.info_popup)
		self.quitBtn.clicked.connect(self.closeEvent)
		self.driveAccountBtn.clicked.connect(self.change_drive_account)
		self.uploadPopup = SingleUploadPopup()


	def single_upload(self):
		def close_popup():
			self.uploadPopup.hide()

		self.connect(self.uploadPopup, QtCore.SIGNAL('close_popup()'), close_popup)
		self.uploadPopup.setFixedSize(300, 300)
		self.uploadPopup.show()


	def change_drive_account(self):
		if os.path.exists("mycreds.txt"):
			os.remove("mycreds.txt")

		self.uploadPopup.drive_startup()


	def select_files(self):
		file_list = QtGui.QFileDialog.getOpenFileNames(self, 'Select Files')  # returns a QStringList object

		for file_name in file_list:
			try:  # only ascii compatible names are read
				fname = str(file_name)  # no bulgarian characters are read
				if fname not in self.filenameList:
					self.filenameList.append(fname)
					fname_base = os.path.basename(fname)
					self.fileListWidget.addItem(fname_base)
			except:
				fname = str(file_name.toUtf8())
				QtGui.QMessageBox.warning(self, 'Error', 'File %s contains non ASCII characters and will, therefore, not be added.' % fname, QtGui.QMessageBox.Ok)


	def clear_file_list(self):
		self.fileListWidget.clear()


	def remove_file_from_list(self):
		item_index = self.fileListWidget.currentRow()
		if item_index != -1:
			self.fileListWidget.takeItem(self.fileListWidget.currentRow()) 
			del self.filenameList[item_index]


	def info_popup(self):
		def close_popup():
			self.infoPopup.hide()

		self.infoPopup = InfoPopup()
		self.connect(self.infoPopup, QtCore.SIGNAL('close_popup()'), close_popup)
		# self.infoPopup.setFixedSize(300, 140)
		self.infoPopup.show()


	def closeEvent(self, evnt):
		# this method overrides the method called when the 'X' of the app is pressed
		# --- pop up message -------
		choice = QtGui.QMessageBox.question(self, 'Quit', 'Are you sure you would like to quit?',
			QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		if choice == QtGui.QMessageBox.Yes:
			sys.exit()
		else:
			evnt.ignore()
			

def main():
	app = QtGui.QApplication(sys.argv)
	app_obj = MainApp()
	app_obj.show()
	app.exec_()

if __name__ == '__main__':
    main()