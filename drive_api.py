# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
import time
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class SingleUploadPopup(QtGui.QWidget):
	drive_folder_dict = {}

	def __init__(self):
		QtGui.QWidget.__init__(self)
		
		self.setWindowTitle("Upload")

		self.scrollArea = QtGui.QScrollArea(self)
		self.scrollArea.setWidgetResizable(True)
		self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 247))
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)

		self.okBtn = QtGui.QPushButton("OK")
		self.okBtn.clicked.connect(self.upload_files)

		self.cancelBtn = QtGui.QPushButton("Cancel")
		self.cancelBtn.clicked.connect(self.close_popup)

		self.verticalLayout = QtGui.QVBoxLayout(self)
		self.verticalLayout.addWidget(self.scrollArea)
		self.verticalLayout.addWidget(self.okBtn)
		self.verticalLayout.addWidget(self.cancelBtn)

		self.verticalLayoutScroll = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)

		self.drive_startup()
		self.load_folder_list()
		# layout = QtGui.QVBoxLayout()
		# layout.addWidget(infoImgLabel)
		# layout.addWidget(okBtn)
		# self.setLayout(layout)


	def drive_startup(self):
		self.gauth = GoogleAuth()
		# check if credentials file exists
		self.gauth.LoadCredentialsFile("mycreds.txt")
		if self.gauth.credentials is None:
		    # Authenticate if they're not there
		    self.gauth.LocalWebserverAuth()
		elif self.gauth.access_token_expired:
		    # Refresh them if expired
		    self.gauth.Refresh()
		else:
		    # Initialize the saved creds
		    self.gauth.Authorize()
		# Save the current credentials to a file
		self.gauth.SaveCredentialsFile("mycreds.txt")

		self.drive = GoogleDrive(self.gauth)


	def load_folder_list(self):
		# obtain a list of drive's folders
		folder_list = self.drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
		for folder in folder_list:
			name_and_ext = os.path.splitext(folder['title'])
			if name_and_ext[1] == '':  # if its a folder and not a file
				# if name_and_ext[0] == 'Uni':
				# 	folder_id = file1['id']
				# print 'title: %s, id: %s' % (name_and_ext[0], file1['id'])
				self.drive_folder_dict[name_and_ext[0]] = folder['id']
				pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
		    	pushButton.setText(name_and_ext[0])

		    	self.verticalLayoutScroll.addWidget(pushButton)


	def upload_files(self):
		# upload files
		self.close_popup()

	def close_popup(self):
		self.emit(QtCore.SIGNAL('close_popup()'))