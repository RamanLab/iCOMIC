import sys
import time
import thread

from PyQt5.QtCore import QObject, pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QInputDialog, QApplication, QProgressDialog

class Message(QObject):
    finished = pyqtSignal()

def createAddress(password, name, obj):
    time.sleep(5)
    obj.finished.emit()


class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        lay = QVBoxLayout(self)
        button = QPushButton("Start processing")
        lay.addWidget(button)
        button.clicked.connect(self.start_task)
        self.message_obj = Message()

    def start_task(self):
        password = "password"
        name, ok = QInputDialog.getText(None, 'Name the address', 'Enter the address name:')
        if ok:
            self.progress_indicator = QProgressDialog(self)
            self.progress_indicator.setWindowModality(Qt.WindowModal)
            self.progress_indicator.setRange(0, 0)
            self.progress_indicator.setAttribute(Qt.WA_DeleteOnClose)
            self.message_obj.finished.connect(self.progress_indicator.close, Qt.QueuedConnection)
            self.progress_indicator.show()
            thread.start_new_thread(createAddress, (password, name, self.message_obj))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    w = Widget()
    w.show()
    sys.exit(app.exec_())