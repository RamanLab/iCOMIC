from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
    QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
import sys
import gzip

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

           
        self.showDialog()
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()


    def showDialog(self):
#        f = open('results_dna/called/TCRBOA-1.vcf', 'r')
        with gzip.open('results_dna/filtered/all.vcf.gz', 'rb') as f:
            data = f.read()
            self.textEdit.setText(data.decode("utf-8"))        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

# =============================================================================
#     def __init__(self):
#         super().__init__()   
# 
#         self.textEdit = QTextEdit()
#         self.setCentralWidget(self.textEdit)
#         self.statusBar()
#         self.initUI()
# 
# 
#     def initUI(self):
# 
# 
#         self.setGeometry(300, 300, 350, 300)
#         self.setWindowTitle("sdff")
# 
# 
#         f = open("/data/Priyanka/other_pipelines/iCOMIC/check_for_correct_filename_check.py", 'r')
# 
#         with f:
#             data = f.read()
#             self.textEdit.setText(data)     
# 
# 
# if __name__ == '__main__':
# 
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
# =============================================================================
