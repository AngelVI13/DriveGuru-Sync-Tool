# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
import os
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class ModListView(QtGui.QListWidget):
    def __init__(self, type, parent=None):
        super(ModListView, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setIconSize(QtCore.QSize(72, 72))

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.emit(QtCore.SIGNAL("dropped"), links)
        else:
            event.ignore()


class Ui_MainWindow(object):
    filenameList = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(419, 377)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 401, 361))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        # --------- Setting to modified listWidget - added drag and drop functionality
        self.fileListWidget = ModListView(self.horizontalLayoutWidget)
        self.fileListWidget.setObjectName(_fromUtf8("fileListWidget"))
        self.connect(self.fileListWidget, QtCore.SIGNAL("dropped"), self.pictureDropped)
        # --------------------
        self.horizontalLayout.addWidget(self.fileListWidget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.driveLogoBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.driveLogoBtn.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("drive.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.driveLogoBtn.setIcon(icon)
        self.driveLogoBtn.setIconSize(QtCore.QSize(96, 96))
        self.driveLogoBtn.setFlat(True)
        self.driveLogoBtn.setObjectName(_fromUtf8("driveLogoBtn"))
        self.verticalLayout.addWidget(self.driveLogoBtn)
        self.uploadBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.uploadBtn.setObjectName(_fromUtf8("uploadBtn"))
        self.verticalLayout.addWidget(self.uploadBtn)
        self.autoUploadBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.autoUploadBtn.setObjectName(_fromUtf8("autoUploadBtn"))
        self.verticalLayout.addWidget(self.autoUploadBtn)
        self.selectFilesBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.selectFilesBtn.setObjectName(_fromUtf8("selectFilesBtn"))
        self.verticalLayout.addWidget(self.selectFilesBtn)
        self.removeFileBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.removeFileBtn.setObjectName(_fromUtf8("removeFileBtn"))
        self.verticalLayout.addWidget(self.removeFileBtn)
        self.clearListBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.clearListBtn.setObjectName(_fromUtf8("clearListBtn"))
        self.verticalLayout.addWidget(self.clearListBtn)
        self.infoBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.infoBtn.setObjectName(_fromUtf8("infoBtn"))
        self.verticalLayout.addWidget(self.infoBtn)
        self.quitBtn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.quitBtn.setObjectName(_fromUtf8("quitBtn"))
        self.verticalLayout.addWidget(self.quitBtn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "DriveGuru", None))
        self.uploadBtn.setText(_translate("MainWindow", "Upload", None))
        self.autoUploadBtn.setText(_translate("MainWindow", "Auto Upload", None))
        self.selectFilesBtn.setText(_translate("MainWindow", "Select Files", None))
        self.removeFileBtn.setText(_translate("MainWindow", "Remove File", None))
        self.clearListBtn.setText(_translate("MainWindow", "Clear List", None))
        self.infoBtn.setText(_translate("MainWindow", "Info", None))
        self.quitBtn.setText(_translate("MainWindow", "Quit", None))


# Implements drag and drop functionality
    def pictureDropped(self, l):
        for url in l:
            if os.path.exists(url):
                print(url)
                if url in self.filenameList:
                    print "item already added"
                else:
                    self.filenameList.append(url)
                    url_base = os.path.basename(url)                
                    icon = QtGui.QIcon(url)
                    pixmap = icon.pixmap(72, 72)                
                    icon = QtGui.QIcon(pixmap)
                    item = QtGui.QListWidgetItem(url_base, self.fileListWidget)
                    item.setIcon(icon)        
                    item.setStatusTip(url)        