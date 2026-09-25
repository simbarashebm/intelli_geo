from qgis.PyQt.QtWidgets import QTextEdit
from qgis.PyQt.QtCore import pyqtSignal, Qt

class MessageEdit(QTextEdit):
    enterPressed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            self.enterPressed.emit()
        else:
            super().keyPressEvent(event)