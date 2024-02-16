from PyQt6 import QtWidgets
from ui_sys import MainWindow
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()