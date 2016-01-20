import sys
from PyQt4.QtGui import *
from src.client.main.core_gui import core_gui

def main():
    app = QApplication(sys.argv)
    ex = core_gui()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()