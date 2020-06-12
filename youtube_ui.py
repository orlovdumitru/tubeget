import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QStyle, QSizePolicy, QFileDialog, QLineEdit
from PyQt5.QtGui import QIcon #, QPalette
from PyQt5.QtCore import Qt, QDir


class TubeGet(QWidget):
    def __init__(self):
        super().__init__()

        # define maine window
        self.setWindowTitle('TubeGet')
        self.setGeometry(350, 100, 700, 200)
        self.setWindowIcon(QIcon('tubeget.png'))

        self.url = QLineEdit()
        self.path_location = QLineEdit()
        download = QPushButton('Donwload')
            
        self.url.setPlaceholderText('URL')
        self.path_location.setPlaceholderText('File save location')

        self.browse_location = QPushButton('Brose...')
        self.browse_location.clicked.connect(self.open_location)
        
        # define main window bacground color
        # p = self.palette()
        # p.setColor(QPalette.Window, Qt.gray)
        # self.setPalette(p)

        self.main_ui()

        self.show()

    def main_ui(self):
        '''Create Window ui'''
        
        # create store location
        # store_path = QPushButton('Browse...')
        # store_path.clicked.connect(self.open_location)
        
        main_v_layout = QVBoxLayout()

        path_h_layout = QHBoxLayout()
        path_h_layout.addWidget(self.path_location)
        path_h_layout.addWidget(self.browse_location)

        main_v_layout.addWidget(self.url)
        main_v_layout.addLayout(path_h_layout)

        self.setLayout(main_v_layout)
        


    def open_location(self):
        file_location = QFileDialog.getSaveFileName(self, caption='Save File As', directory='.', filter='All Files(*.*)')
        self.path_location.setText(QDir.toNativeSeparators(file_location[0]))

    

app = QApplication(sys.argv)
tg = TubeGet()
sys.exit(app.exec_()) 
