from PyQt5.QtWidgets import QDialog
from src.fiberfit_gui import error_dialog as ErrorDialog

class ErrorDialog(QDialog, ErrorDialog.Ui_ErrorDialog):
    def __init__(self, parent=None, screenDim = None):
        super(ErrorDialog, self).__init__(parent)
        self.setupUi(self, screenDim)

    def show(self):
        self.exec_()