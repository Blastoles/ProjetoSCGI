from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QDialog
from functools import partial
from View.V



class SistemaImpressora():
    def Show(self):
        self.impressora.Show()

    def __init__(self):
        self.impressora = viewMenu()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Atribuindo o objeto
    menu = ()

    # Show das telas
    menu.tela.show()
    sys.exit(app.exec())
