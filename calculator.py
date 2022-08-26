import imp
from itertools import takewhile, dropwhile
from math import sqrt
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy



        
def fmt_display(str):
    str  = str.replace('÷', '/')
    str  = str.replace('x', '*')
    str  = str.replace('mod', '%')
    str  = str.replace('^', '**')

    return str


class Calculator(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator')
        self.colorCount()
        self.setFixedSize(320,350)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0 ,0, 1, 5)
        self.display.setDisabled(True)
        self.setStyleSheet(
            '*{background: #FFF; color: black; font-size: 25px}'
        )

        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        
        self.add_btn(
            QPushButton('<-'), 1, 0, 1, 1,
                lambda: self.display.setText(
                    self.display.text()[:-1]
                ),
                'background: #791515; color: white')
        self.add_btn(QPushButton('('), 1, 1, 1, 1)
        self.add_btn(QPushButton(')'), 1, 2, 1, 1)
        self.add_btn(QPushButton('^'), 1, 3, 1, 1)

        self.add_btn(QPushButton('7'), 2, 0, 1, 1)
        self.add_btn(QPushButton('8'), 2, 1, 1, 1)
        self.add_btn(QPushButton('9'), 2, 2, 1, 1)
        self.add_btn(QPushButton('÷'), 2, 3, 1, 1)
        self.add_btn(QPushButton('4'), 3, 0, 1, 1)
        self.add_btn(QPushButton('5'), 3, 1, 1, 1)
        self.add_btn(QPushButton('6'), 3, 2, 1, 1)
        self.add_btn(QPushButton('x'), 3, 3, 1, 1)
        self.add_btn(QPushButton('1'), 4, 0, 1, 1)
        self.add_btn(QPushButton('2'), 4, 1, 1, 1)
        self.add_btn(QPushButton('3'), 4, 2, 1, 1)
        self.add_btn(QPushButton('-'), 4, 3, 1, 1)
        self.add_btn(QPushButton('0'), 5, 0, 1, 2)
        self.add_btn(QPushButton('.'), 5, 2, 1, 1)
        self.add_btn(QPushButton('+'), 5, 3, 1, 1)
        
        self.add_btn( 
            QPushButton('C'), 1, 4, 1, 1, 
                lambda: self.display.setText(''),
                'background: #0000ff; color: white')

        self.add_btn(QPushButton('mod'), 2, 4, 1, 1,'','font-size: 16px')
        self.add_btn(
            QPushButton('='), 5, 4, 1, 1, self.equal_method,
                'background: #135e0d; color: white')
        self.add_btn(QPushButton('√'), 3, 4, 1, 1, 
            lambda: self.display.setText(
                str(sqrt(int(self.display.text())))
                ))
        self.add_btn(QPushButton('%'), 4, 4, 1, 1, 
            lambda: self.display.setText(
                str(self.percent_method())
            ))

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan, function=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not function:
                btn.clicked.connect(
                    lambda: self.display.setText(
                        self.display.text() + btn.text()
                ))

        else:
            btn.clicked.connect(function)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        
    def equal_method(self):
        try:
            self.display.setText(
                str(eval(fmt_display(self.display.text())))
            )
        except Exception as error:
            self.display.setText('ERROR')

    def percent_method(self):
        new_str   = list(self.display.text())
        percent   = ''.join(list(takewhile(lambda x: x != 'x', reversed(new_str)))) 
        f_percent = ''.join(list(reversed(percent)))
        value     = ''.join(list(dropwhile(lambda x: x != 'x', reversed(new_str))))
        f_value   = ''.join(list(reversed(value)))[:-1]
        
        try:
            self.display.setText(str(int(eval(f_value))*int(f_percent)/100))

        except Exception as error:
            self.display.setText('ERROR')






if __name__ == '__main__':
    qt   = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    qt.exec()

