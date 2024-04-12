import sys
from PySide6.QtWidgets import QApplication
from TatarTeleTranslit.main_window.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setApplicationName('TatarTeleTranslit')

    main_window = MainWindow()
    main_window.show()

    app.exec()

if __name__ == '__main__':
    main()
