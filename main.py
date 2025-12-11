#(Easy) Editor!
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PyQt5.QtWidgets import QPushButton, QLabel, QListWidget
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter
import os
#
class ImageProcessor():
    #Basic
    def __init__(self):
        self.image = None
        self.fileName = None
        self.modifiedFolder = "Modified_Images/"
        self.modifiedImage = self.image

    def loadImage(self, fileName):
        self.fileName = fileName
        image_path = os.path.join(workingFolder, fileName)
        self.image = Image.open(image_path)
        self.modifiedImage = self.image

    def showImage(self, imagePath):
        lImage.hide()
        pixmapImage = QPixmap(imagePath)
        width, height = lImage.width(), lImage.height()
        pixmapImage = pixmapImage.scaled(width, height, Qt.KeepAspectRatio)
        lImage.setPixmap(pixmapImage)
        lImage.show()
     
    def saveImage(self,modifiedImage):
        if os.path.isdir(os.path.join(workingFolder, self.modifiedFolder)) == False:
            os.mkdir(os.path.join(workingFolder, self.modifiedFolder))
        modifiedImage.save(os.path.join(os.path.join(workingFolder, self.modifiedFolder), self.fileName))

    #Changers
    def blackWhite(self):
        try:
            if self.modifiedImage != None:
                self.modifiedImage = self.modifiedImage.convert("L")
            else:
                self.modifiedImage = self.image.convert("L")
            self.saveImage(self.modifiedImage)
            self.showImage(os.path.join(os.path.join(workingFolder, self.modifiedFolder), self.fileName))
        except:
            mb = QMessageBox()
            mb.setWindowTitle("Error")
            mb.setText("Select any Image in list.\nIf list empty select folder with images")
            mb.exec_()

    def sharpness(self):
        try:
            if self.modifiedImage != None:
                self.modifiedImage = self.modifiedImage.filter(ImageFilter.BLUR)
            else:
                self.modifiedImage = self.image.filter(ImageFilter.BLUR)
            self.saveImage(self.modifiedImage)
            self.showImage(os.path.join(os.path.join(workingFolder, self.modifiedFolder), self.fileName))
        except:
            mb = QMessageBox()
            mb.setWindowTitle("Error")
            mb.setText("Select any Image in list.\nIf list empty select folder with images")
            mb.exec_()
    
    def mirror(self):
        try:
            if self.modifiedImage != None:
                self.modifiedImage = self.modifiedImage.transpose(Image.FLIP_LEFT_RIGHT)
            else:
                self.modifiedImage = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.saveImage(self.modifiedImage)
            self.showImage(os.path.join(os.path.join(workingFolder, self.modifiedFolder), self.fileName))
        except:
            mb = QMessageBox()
            mb.setWindowTitle("Error")
            mb.setText("Select any Image in list.\nIf list empty select folder with images")
            mb.exec_()

    def right(self):
        try:
            if self.modifiedImage != None:
                self.modifiedImage = self.modifiedImage.transpose(Image.ROTATE_270)
            else:
                self.modifiedImage = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.saveImage(self.modifiedImage)
            self.showImage(os.path.join(os.path.join(workingFolder, self.modifiedFolder), self.fileName))
        except:
            mb = QMessageBox()
            mb.setWindowTitle("Error")
            mb.setText("Select any Image in list.\nIf list empty select folder with images")
            mb.exec_()

    def left(self):
        try:
            if self.modifiedImage != None:
                self.modifiedImage = self.modifiedImage.transpose(Image.ROTATE_90)
            else:
                self.modifiedImage = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.saveImage(self.modifiedImage)
            self.showImage(os.path.join(os.path.join(workingFolder, self.modifiedFolder), self.fileName))
        except:
            mb = QMessageBox()
            mb.setWindowTitle("Error")
            mb.setText("Select any Image in list.\nIf list empty select folder with images")
            mb.exec_()

workingFolder = ""
def changeDir():
    userInput = QFileDialog.getExistingDirectory()
    global workingFolder
    workingFolder = userInput

def filter(files, extensions):
    exitFiles = []
    for fileName in files:
        for extension in extensions:
            if fileName.endswith(extension):
                exitFiles.append(fileName)
    return exitFiles

def showFilenamesList():
    changeDir()
    if workingFolder != "":
        extensions = [".png",".jpg",".jpeg",".gif",".bmp"]
        filteredFiles = filter(os.listdir(workingFolder),extensions)
        listFolders.clear()
        listFolders.addItems(filteredFiles)

def showChosenImage():
    if listFolders.currentRow() >= 0:
        fileName = listFolders.currentItem().text()
        currentImage.loadImage(fileName)
        image_path = os.path.join(workingFolder, currentImage.fileName)
        currentImage.showImage(image_path)

#
app = QApplication([])
window = QWidget()
window.setWindowTitle("Easy Editor")
window.resize(600,400)
#
bFolder = QPushButton("Folder")
bLeft = QPushButton("Left")
bRight = QPushButton("Right")
bMirror = QPushButton("Mirror")
bSharpness = QPushButton("Sharpness")
bBlackWhite = QPushButton("Black/White")
listFolders = QListWidget()
lImage = QLabel("<Image>")

vLineFolders = QVBoxLayout()
vLineTools = QVBoxLayout()
hLineTools = QHBoxLayout()
hLineMain = QHBoxLayout()
#
hLineTools.addWidget(bLeft)
hLineTools.addWidget(bRight)
hLineTools.addWidget(bMirror)
hLineTools.addWidget(bSharpness)
hLineTools.addWidget(bBlackWhite)

vLineFolders.addWidget(bFolder)
vLineFolders.addWidget(listFolders)

vLineTools.addWidget(lImage)
vLineTools.addLayout(hLineTools)

hLineMain.addLayout(vLineFolders)
hLineMain.addLayout(vLineTools)
#
currentImage = ImageProcessor()
#
listFolders.currentRowChanged.connect(showChosenImage)
bFolder.clicked.connect(showFilenamesList)
bBlackWhite.clicked.connect(currentImage.blackWhite)
bSharpness.clicked.connect(currentImage.sharpness)
bMirror.clicked.connect(currentImage.mirror)
bLeft.clicked.connect(currentImage.left)
bRight.clicked.connect(currentImage.right)
#
window.setLayout(hLineMain)
window.show()
app.exec_()