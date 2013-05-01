import sys
from PySide import QtGui, QtCore

class Editor(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        self.setWindowTitle("Editor de Texto")
        self.resize(640, 480)
        
        self.txtEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.txtEdit)
        
        self.statusBar().showMessage("Listo", 5000)
        
        openFile = QtGui.QAction("&Abrir", self)
        openFile.setShortcut(QtGui.QKeySequence.Open)
        openFile.setStatusTip("Abrir un archivo")
        
        newFile = QtGui.QAction("&Nuevo", self)
        newFile.setShortcut(QtGui.QKeySequence.New)
        newFile.setStatusTip("Crear un archivo nuevo")
        
        saveFile = QtGui.QAction("&Guardar", self)
        saveFile.setShortcut(QtGui.QKeySequence.Save)
        saveFile.setStatusTip("Guardar el archivo")
        
        saveAsFile = QtGui.QAction("G&uardar como", self)
        saveAsFile.setShortcut(QtGui.QKeySequence.SaveAs)
        saveAsFile.setStatusTip("Guardar el archivo como")
        
        closeApp = QtGui.QAction("&Salir", self)
        closeApp.setShortcut(QtGui.QKeySequence.Close)
        closeApp.setStatusTip("Salir de la aplicacion")
        
        openFile.triggered.connect(self.openFile)
        newFile.triggered.connect(self.newFile)
        saveFile.triggered.connect(self.saveFile)
        saveAsFile.triggered.connect(self.saveAsFile)
        closeApp.triggered.connect(self.close)
        
        undoEdit = QtGui.QAction("&Deshacer", self)
        undoEdit.setShortcut(QtGui.QKeySequence.Undo)
        undoEdit.setStatusTip("Deshacer")
        
        redoEdit = QtGui.QAction("&Rehacer", self)
        redoEdit.setShortcut(QtGui.QKeySequence.Redo)
        redoEdit.setStatusTip("Rehacer")
        
        cutText = QtGui.QAction("C&ortar", self)
        cutText.setShortcut(QtGui.QKeySequence.Cut)
        cutText.setStatusTip("Cortar")
        
        copyText = QtGui.QAction("&Copiar", self)
        copyText.setShortcut(QtGui.QKeySequence.Copy)
        copyText.setStatusTip("Copiar")
        
        pasteText = QtGui.QAction("&Pegar", self)
        pasteText.setShortcut(QtGui.QKeySequence.Paste)
        pasteText.setStatusTip("Pegar")
        
        selectAll = QtGui.QAction("&Seleccionar todo", self)
        selectAll.setShortcut(QtGui.QKeySequence.SelectAll)
        selectAll.setStatusTip("Seleccionar todo")
        
        undoEdit.triggered.connect(self.txtEdit.undo)
        redoEdit.triggered.connect(self.txtEdit.redo)
        cutText.triggered.connect(self.txtEdit.cut)
        copyText.triggered.connect(self.txtEdit.copy)
        pasteText.triggered.connect(self.txtEdit.paste)
        selectAll.triggered.connect(self.txtEdit.selectAll)
        
        formatText = QtGui.QAction("&Formato", self)
        formatText.setStatusTip("Formato de texto")
        
        formatText.triggered.connect(self.formatText)
        
        menubar = QtGui.QMenuBar()
        fileMenu = QtGui.QMenu("&Archivo")
        editMenu = QtGui.QMenu("&Edicion")
        formatMenu = QtGui.QMenu("&Formato")
        fileMenu.addAction(openFile)
        fileMenu.addAction(newFile)
        fileMenu.addSeparator()
        fileMenu.addAction(saveFile)
        fileMenu.addAction(saveAsFile)
        fileMenu.addSeparator()
        fileMenu.addAction(closeApp)
        editMenu.addAction(undoEdit)
        editMenu.addAction(redoEdit)
        editMenu.addSeparator()
        editMenu.addAction(cutText)
        editMenu.addAction(copyText)
        editMenu.addAction(pasteText)
        editMenu.addSeparator()
        editMenu.addAction(selectAll)
        formatMenu.addAction(formatText)
        menubar.addMenu(fileMenu)
        menubar.addMenu(editMenu)
        menubar.addMenu(formatMenu)
        self.setMenuBar(menubar)    
    
    def openFile(self):
        try:
            self.filename = QtGui.QFileDialog.getOpenFileName(self, "Abrir archivo")
            self.setWindowTitle("Editor de Texto - %s" % self.filename[0])
            f = open(self.filename[0])
            self.txtEdit.setText(f.read())
        except:
            self.setWindowTitle("Editor de Texto")
    
    def newFile(self):
        self.e = Editor()
        self.e.show()
    
    def saveFile(self):
        try:
            f = open(self.filename[0], "w")
            f.write(self.txtEdit.toPlainText())
        except:
            try:
                self.filename = QtGui.QFileDialog.getSaveFileName(self, "Guardar archivo")
                self.setWindowTitle("Editor de Texto - %s" % self.filename[0])
                f = open(self.filename[0], "w")
                f.write(self.txtEdit.toPlainText())
            except:
                self.setWindowTitle("Editor de Texto")
    
    def saveAsFile(self):
        try:
            self.filename = QtGui.QFileDialog.getSaveFileName(self, "Guardar archivo como")
            self.setWindowTitle("Editor de Texto - %s" % self.filename[0])
            f = open(self.filename[0], "w")
            f.write(self.txtEdit.toPlainText())
        except:
            self.setWindowTitle("Editor de Texto")
    
    def formatText(self):
        (font, ok) = QtGui.QFontDialog.getFont()
        if ok:
            self.txtEdit.setFont(font)
        else:
            pass

app = QtGui.QApplication(sys.argv)
e = Editor()
e.show()
sys.exit(app.exec_())