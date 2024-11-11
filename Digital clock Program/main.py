import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class Digitalclock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(700, 400, 300, 100)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        
        self.time_label.setAlignment(Qt.AlignCenter)
        
        self.time_label.setStyleSheet("font-size: 80px;"
                                      "color : hsl(136, 98%, 55%);")
        self.setStyleSheet("background-color: black;")
        
        font_id = QFontDatabase.addApplicationFont("Digital clock Program/DS-DIGIB.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        my_clock_font = QFont(font_family, 150)
        self.time_label.setFont(my_clock_font)
        
        
        self.update_time()
        
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)
        
        
        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = Digitalclock()
    clock.show()
    sys.exit(app.exec_())
    