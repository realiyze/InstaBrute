
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import webbrowser
import core
import subprocess

class Widget1(QWidget):
    def __init__(self, parent=None):
        super(Widget1, self).__init__(parent)
        self.gui()

    def gui(self):
        self.w1 = self
        self.w1.setAutoFillBackground(True)
        self.w1.setWindowTitle("InstaBrute v1")
        self.w1.resize(380, 540)
        self.w1.setCursor(Qt.ArrowCursor)
        self.w1.setToolTip("")
        self.label1 = QLabel(self.w1)
        self.label1.setText("Username")
        self.label1.move(20, 90)
        self.label1.resize(50, 22)
        self.label1.setCursor(Qt.ArrowCursor)
        self.label1.setToolTip("")
        self.instausername = QLineEdit(self.w1)
        self.instausername.setText("")
        self.instausername.move(90, 90)
        self.instausername.resize(110, 22)
        self.instausername.setCursor(Qt.IBeamCursor)
        self.instausername.setToolTip("")
        self.minpass = QSpinBox(self.w1)
        self.minpass.setMinimum(0)
        self.minpass.setMaximum(100)
        self.minpass.setSingleStep(1)
        self.minpass.setValue(0)
        self.minpass.move(130, 120)
        self.minpass.resize(40, 22)
        self.minpass.setCursor(Qt.ArrowCursor)
        self.minpass.setToolTip("")
        self.label2 = QLabel(self.w1)
        self.label2.setText("Min Password Range")
        self.label2.move(20, 120)
        self.label2.resize(100, 22)
        self.label2.setCursor(Qt.ArrowCursor)
        self.label2.setToolTip("")
        self.label2_copy = QLabel(self.w1)
        self.label2_copy.setText("Max Password Range")
        self.label2_copy.move(20, 150)
        self.label2_copy.resize(110, 22)
        self.label2_copy.setCursor(Qt.ArrowCursor)
        self.label2_copy.setToolTip("")
        self.maxpass = QSpinBox(self.w1)
        self.maxpass.setMinimum(0)
        self.maxpass.setMaximum(100)
        self.maxpass.setSingleStep(1)
        self.maxpass.setValue(0)
        self.maxpass.move(130, 150)
        self.maxpass.resize(40, 22)
        self.maxpass.setCursor(Qt.ArrowCursor)
        self.maxpass.setToolTip("")
        self.label3 = QLabel(self.w1)
        self.label3.setText("Timeout")
        self.label3.move(20, 210)
        self.label3.resize(50, 22)
        self.label3.setCursor(Qt.ArrowCursor)
        self.label3.setToolTip("")
        self.timeout1 = QSpinBox(self.w1)
        self.timeout1.setMinimum(0)
        self.timeout1.setMaximum(100)
        self.timeout1.setSingleStep(1)
        self.timeout1.setValue(0)
        self.timeout1.move(130, 210)
        self.timeout1.resize(40, 22)
        self.timeout1.setCursor(Qt.ArrowCursor)
        self.timeout1.setToolTip("")
        self.button1 = QToolButton(self.w1)
        self.button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button1.setText("Start Attack")
        self.button1.move(200, 240)
        self.button1.resize(160, 42)
        self.button1.setCursor(Qt.ArrowCursor)
        self.button1.setToolTip("")
        self.button1.clicked.connect(self.start_attack)
        self.results = QPlainTextEdit(self.w1)
        self.results.setPlainText("")
        self.results.move(10, 330)
        self.results.resize(360, 160)
        self.results.setCursor(Qt.ArrowCursor)
        self.results.setToolTip("")
        self.button2 = QToolButton(self.w1)
        self.button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button2.setText("")
        button2_pixmap = QPixmap("aparat.jpg")
        self.button2.setAutoRaise(True)
        self.button2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.button2.setIconSize(button2_pixmap.size())
        self.button2.setIcon(QIcon(button2_pixmap))
        self.button2.move(330, 490)
        self.button2.resize(40, 42)
        self.button2.setCursor(Qt.ArrowCursor)
        self.button2.setToolTip("")
        self.button2.clicked.connect(self.aparat)
        self.button3 = QToolButton(self.w1)
        self.button3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button3.setText("")
        button3_pixmap = QPixmap("github.jpg")
        self.button3.setAutoRaise(True)
        self.button3.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.button3.setIconSize(button3_pixmap.size())
        self.button3.setIcon(QIcon(button3_pixmap))
        self.button3.move(290, 490)
        self.button3.resize(40, 42)
        self.button3.setCursor(Qt.ArrowCursor)
        self.button3.setToolTip("")
        self.button3.clicked.connect(self.github)
        self.button4 = QToolButton(self.w1)
        self.button4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button4.setText("")
        button4_pixmap = QPixmap("insta.jpg")
        self.button4.setAutoRaise(True)
        self.button4.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.button4.setIconSize(button4_pixmap.size())
        self.button4.setIcon(QIcon(button4_pixmap))
        self.button4.move(250, 490)
        self.button4.resize(40, 42)
        self.button4.setCursor(Qt.ArrowCursor)
        self.button4.setToolTip("")
        self.button4.clicked.connect(self.instagram)
        self.label4 = QLabel(self.w1)
        self.label4.setText("CopyRight (C) HaniSoftwares 2019-2023")
        self.label4.move(10, 500)
        self.label4.resize(210, 22)
        self.label4.setCursor(Qt.ArrowCursor)
        self.label4.setToolTip("")
        self.image5 = QLabel(self.w1)
        self.image5.setPixmap(QPixmap("logo.png"))
        self.image5.move(40, 0)
        self.image5.resize(301, 71)
        self.image5.setAutoFillBackground(True)
        palette = self.image5.palette()
        palette.setColor(self.image5.backgroundRole(), QColor(255, 255, 255, 255))
        self.image5.setPalette(palette)
        self.image5.setCursor(Qt.ArrowCursor)
        self.image5.setToolTip("")
        self.radio1 = QRadioButton("Random Brute", self.w1)
        self.radio1.setChecked(1)
        self.radio1.move(20, 180)
        self.radio1.resize(90, 22)
        self.radio1.setCursor(Qt.ArrowCursor)
        self.radio1.setToolTip("")
        self.radio1.clicked.connect(self.checked_random)
        self.radio2 = QRadioButton("Dictionary Brute", self.w1)
        self.radio2.setChecked(0)
        self.radio2.move(110, 180)
        self.radio2.resize(100, 22)
        self.radio2.setCursor(Qt.ArrowCursor)
        self.radio2.setToolTip("")
        self.radio2.clicked.connect(self.checked_passlist)
        self.passwordlist = QLineEdit(self.w1)
        self.passwordlist.setText("")
        self.passwordlist.move(200, 150)
        self.passwordlist.resize(160, 22)
        self.passwordlist.setCursor(Qt.IBeamCursor)
        self.passwordlist.setToolTip("")
        self.passwordlist.setEnabled(False)
        self.label5 = QLabel(self.w1)
        self.label5.setText("Drag Password List Below")
        self.label5.move(200, 120)
        self.label5.resize(130, 22)
        self.label5.setCursor(Qt.ArrowCursor)
        self.label5.setToolTip("")
        self.label6 = QLabel(self.w1)
        self.label6.setText("Blocked By Instagram?")
        self.label6.move(20, 240)
        self.label6.resize(120, 22)
        self.label6.setCursor(Qt.ArrowCursor)
        self.label6.setToolTip("")
        self.button6 = QToolButton(self.w1)
        self.button6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button6.setText("Use A VPN")
        self.button6.move(20, 260)
        self.button6.resize(110, 22)
        self.button6.setCursor(Qt.ArrowCursor)
        self.button6.setToolTip("")
        self.button6.clicked.connect(self.vpnbook)
        return self.w1

    def start_attack(self):
        username = self.instausername.text(scorelordd)
        min_pass_length = self.minpass.value()
        max_pass_length = self.maxpass.value()
        timeout = self.timeout1.value()
        password_list = self.passwordlist.text()
        if self.radio1.isChecked():
            core.instabrute(username, min_pass_length, max_pass_length, timeout, output=self.results)
        elif self.radio2.isChecked():
            core.instabrute_passlist(username, password_list, timeout, output=self.results)
        else:
            self.results.insertPlainText("Please Select A Brute Force Method")

    def aparat(self):
        webbrowser.open_new("aparat.com/hanicraft2")

    def github(self):
        webbrowser.open_new("github.com/hanicraft")

    def instagram(self):
        webbrowser.open_new("instagram.com/mohamadhanijanaty85")

    def checked_random(self):
        self.passwordlist.setDisabled(True)
        self.minpass.setEnabled(True)
        self.maxpass.setEnabled(True)

    def checked_passlist(self):
        self.passwordlist.setEnabled(True)
        self.minpass.setDisabled(True)
        self.maxpass.setDisabled(True)

    def vpnbook(self):
        subprocess.Popen("cmd.exe /K python vpn.py")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    a = Widget1()
    a.show()
    sys.exit(app.exec_())
