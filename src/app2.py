from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QAction,QFileDialog,QWidget 	# GUI components
from PyQt5.QtGui import *																		# QPixmap for images
from PyQt5.QtCore import pyqtSlot																# For linking 
import os																						# For directory handling 
import sys																						# For exititng application
import subprocess 																				# For shell commands
import basics																					# Basic string handling

class MyWindow(QMainWindow,QWidget):
	def __init__(self):
		super(MyWindow,self).__init__()
		self.setGeometry(500,500,600,600)
		self.initUI()
	
	def initUI(self):
		self.label = QtWidgets.QLabel(self)
		self.label.setText("")
		self.label.setGeometry(250,250,100,100)

		# Select Image button
		self.selectImageButton = QtWidgets.QPushButton(self)
		self.selectImageButton.setText("Select Image")
		self.selectImageButton.move(250,400)
		self.selectImageButton.clicked.connect(self.getImageFile)

		# Create open action
		openAction = QAction(QIcon('new.png'), '&Open', self)
		openAction.setShortcut('Ctrl+O')
		openAction.setStatusTip('Open File')
		openAction.triggered.connect(self.getImageFile)

		# Create build action
		buildAction = QAction(QIcon('new.png'), '&Build', self)
		buildAction.setShortcut('Ctrl+B')
		buildAction.setStatusTip('Build Code')
		buildAction.triggered.connect(self.buildCall)

		# Create run action
		runAction = QAction(QIcon('new.png'), '&Build and Run', self)
		runAction.setShortcut('Ctrl+F9')
		runAction.setStatusTip('Build and Run Code')
		runAction.triggered.connect(self.runCall)

		# Create exit action
		exitAction = QAction(QIcon('exit.png'), '&Exit', self)
		exitAction.setShortcut('Alt + F4')
		exitAction.setStatusTip('Exit Application')
		exitAction.triggered.connect(self.exitCall)

		# Menu bar
		menuBar = self.menuBar()
		menuBar.setNativeMenuBar(False)
		fileMenu = menuBar.addMenu('&File')
		fileMenu.addAction(openAction)
		fileMenu.addAction(buildAction)
		fileMenu.addAction(runAction)
		fileMenu.addAction(exitAction)

	# Method for Select Image button
	"""def clicked(self):
		self.label.setText("Button Clicked")
		self.update()

	# Method for label
	def update(self):
		self.label.adjustSize()"""

		

	# Menu bar action methods

	def buildCall(self):
		
		path = QFileDialog.getOpenFileName(self, 'Open file', 
		 '/home/saswat/',"linux shell scripts (*.sh)")
		fileName = basics.getFileNameFromPath(path[0])
		buildPath = basics.removeFileNameFromPath(path[0],fileName)
		os.chdir(buildPath)
		buildCommand = "bash " + fileName
		subprocess.call(buildCommand,shell = True)
		
		#print("\nFilename = " + fileName)
		#print("\nbuildPath = " + buildPath)
		#print("\nbuildCommand = " + buildCommand)

	def runCall(self):
		path = QFileDialog.getOpenFileName(self, 'Open file', 
		 '/home/saswat/',"linux shell scripts (*.sh)")
		fileName = basics.getFileNameFromPath(path[0])
		buildPath = basics.removeFileNameFromPath(path[0],fileName)
		runCommand = "bash " + fileName
		os.chdir(buildPath)
		subprocess.call(runCommand,shell = True)
	
	def exitCall(self):
		print("\nExited Application")
		sys.exit(app.exec_())

	# Connected to Select Image button and openAction
	def getImageFile(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', 
		 '/home/saswat/',"Image files (*.png)")
		#print("Image name = "+str(fname[0]))
		image = QPixmap(fname[0])
		image = image.scaled(100,100)
		self.label.setPixmap(image)




def window():
	app = QApplication(sys.argv)
	win = MyWindow()
	win.show()
	sys.exit(app.exec_())

window()

