import sys

import pandas as pd
from PyQt5 import QtCore, QtWidgets

import Extras.Gen_plot.headerfind as hf


def fileimport(file_source):

    # file_source = input('Enter file path: ')
    head_row = hf.head(file_source)
    print(head_row)

    if '.csv' in str(file_source):
        file_data = pd.read_csv(file_source, header=head_row)
    elif '.xls' in str(file_source):
        file_data = pd.read_excel(file_source, sheetname=head_row[1], header=head_row[0])

    listofelements = (file_data.columns.values)

    return file_data, listofelements



class MyListWidget(QtWidgets.QListWidget):

    fileDropped = QtCore.pyqtSignal(list)

    def __init__(self, parent):
        super(MyListWidget, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(MyListWidget, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        super(MyListWidget, self).dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
              file_path = []
              for url in event.mimeData().urls():
                self.addItem(url.path())
                file_path.append(url.path())
              self.fileDropped.emit(file_path)
              event.acceptProposedAction()
        else:
          super(MyListWidget,self).dropEvent(event)


class MyComboBox(QtWidgets.QComboBox):
    def __init__(self, parent):
        super(MyComboBox, self).__init__(parent)

        # combobox dropdown display for X

        self.header_option_x = QtWidgets.QLabel("Select X data", self)

        comboBox = QtWidgets.QComboBox(self)
        for elementx in processed_file[1]:
            comboBox.addItem(elementx)

        comboBox.move(50, 40)

        self.header_option_x.move(50, 10)
        comboBox.activated[str].connect(self.headeroptionx)

        # ~ combobox dropdown display for X

        # combobox dropdown display for Y1

        self.header_option_y1 = QtWidgets.QLabel("Select Y1 data", self)

        comboBox = QtWidgets.QComboBox(self)
        for elementy1 in processed_file[1]:
            comboBox.addItem(elementy1)

        comboBox.move(200, 40)

        self.header_option_y1.move(200, 10)
        comboBox.activated[str].connect(self.headeroptiony1)

        # ~ combobox dropdown display for Y1

        # combobox dropdown display for Y2

        self.header_option_y2 = QtWidgets.QLabel("Select Y2 data", self)

        comboBox = QtWidgets.QComboBox(self)
        for elementy2 in processed_file[1]:
            comboBox.addItem(elementy2)

        comboBox.move(350, 40)

        self.header_option_y2.move(350, 10)
        comboBox.activated[str].connect(self.headeroptiony2)

        # ~ combobox dropdown display for Y1

    def headeroptionx(self, text):
        self.header_option_x.setText(text)

    def headeroptiony1(self, text):
        self.header_option_y1.setText(text)

    def headeroptiony2(self, text):
        self.header_option_y2.setText(text)



class Window(QtWidgets.QMainWindow):


    # def home(self):
    #
    #     self.dndfilename = MyListWidget(self)
    #     # self.dndfilename.move(50, 100)
    #     self.dndfilename.setGeometry(100, 80, 250, 40)
    #     self.dndfilename.fileDropped.connect(self.testfunc)

    def testfunc(self, l):
        for url in l:
            print(url)




        # self.show()



    # def dndaction(self, text):
    #     self.filename = text
    #     print(self.filename)


    def __init__(self):
        super(Window, self).__init__()

        # main window display
        self.setGeometry(0, 0, 500, 300)
        self.move(300, 300)
        self.setWindowTitle("Plot GUI")

        self.dndfilename = MyListWidget(self)
        # self.dndfilename.move(50, 100)
        self.dndfilename.setGeometry(100, 80, 250, 40)
        self.dndfilename.fileDropped.connect(self.testfunc)

        # self.home()
        self.show()


def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
