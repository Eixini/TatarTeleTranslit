from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon
from TatarTeleTranslit.main_window.ui_gen.ui_main_window import Ui_MainWindow
from TatarTeleTranslit.resource import icons_rc


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Tatar Tele Translit')
        self.setWindowIcon(QIcon(':/icons/ttt.png'))

        self.ui.target_textedit.setVisible(False)

        self.ui.source_combobox.addItem('Кирилл хәрефе','cyr')
        self.ui.source_combobox.addItem('Latin xӓrefe', 'lat')

        self.ui.target_combobox.addItem('Кирилл хәрефе', 'cyr')
        self.ui.target_combobox.addItem('Latin xӓrefe', 'lat')

        self.cyr_to_lat_lowercase = {
            'а': 'a',
            'ә': 'ӓ',
            'б': 'b',
            'в': 'v',
            'г': 'g',
            'д': 'd',
            'е': 'e',
            'ё': 'yo',
            'ж': 'j',
            'җ': 'c',
            'з': 'z',
            'и': 'i',
            'й': 'y',
            'к': 'k',
            'л': 'l',
            'м': 'm',
            'н': 'n',
            'ң': 'ñ',
            'о': 'o',
            'ө': 'ö',
            'п': 'p',
            'р': 'r',
            'с': 's',
            'т': 't',
            'у': 'u',
            'ү': 'ü',
            'ф': 'f',
            'х': 'x',
            'һ': 'h',
            'ц': 'ts',
            'ч': 'ç',
            'ш': 'ş',
            'щ': 'tsh',
            'ъ': '',
            'ь': '',
            'ы': 'ı',
            'э': '\'',
            'ю': 'yu',
            'я': 'ya',
        }

        self.cyr_to_lat_uppercase = {
            'А': 'A',
            'Ә': 'Ӓ',
            'Б': 'B',
            'В': 'V',
            'Г': 'G',
            'Д': 'D',
            'E': 'E',
            'Ё': 'Yo',
            'Ж': 'J',
            'Җ': 'C',
            'З': 'Z',
            'И': 'İ',
            'Й': 'Y',
            'К': 'K',
            'Л': 'L',
            'М': 'M',
            'Н': 'N',
            'Ң': 'Ñ',
            'О': 'O',
            'Ө': 'Ö',
            'П': 'P',
            'Р': 'R',
            'С': 'S',
            'Т': 'T',
            'У': 'U',
            'Ү': 'Ü',
            'Ф': 'F',
            'Х': 'X',
            'Һ': 'H',
            'Ц': 'Ts',
            'Ч': 'Ç',
            'Ш': 'Ş',
            'Щ': 'Tsh',
            'Ъ': '',
            'Ь': '',
            'Ы': 'I',
            'Э': '\'',
            'Ю': 'Yu',
            'Я': 'Ya',
        }

        self.ui.translit_button.clicked.connect(self.translit)
        self.ui.source_textedit.textChanged.connect(self.source_textedit_changed)

    def source_textedit_changed(self):
        self.ui.target_textedit.clear()
        self.ui.target_textedit.setVisible(False)

    def translit(self):
 
        if not self.ui.source_textedit.toPlainText() == '':

            buffer = self.ui.source_textedit.toPlainText()

            if (self.ui.source_combobox.currentData() == 'cyr'
                and self.ui.target_combobox.currentData() == 'lat'):

                for char in buffer:
                    for key, value in self.cyr_to_lat_uppercase.items():
                        if char == key:
                            buffer = buffer.replace(char, self.cyr_to_lat_uppercase[key])
                    for key, value in self.cyr_to_lat_lowercase.items():
                        if char == key:
                            buffer = buffer.replace(char, self.cyr_to_lat_lowercase[key])

            if (self.ui.source_combobox.currentData() == 'lat'
                and self.ui.target_combobox.currentData() == 'cyr'):
                
                for char in buffer:
                    for key, value in self.cyr_to_lat_uppercase.items():
                        if char == value:
                            buffer = buffer.replace(char, key)
                            print(buffer)
                    for key, value in self.cyr_to_lat_lowercase.items():
                        if char == value:
                            buffer = buffer.replace(char, key)
                            print(buffer)

            self.ui.target_textedit.setPlainText(buffer)
            self.ui.target_textedit.setVisible(True)
