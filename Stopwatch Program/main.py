import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt, QTime, QTimer


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.timer = QTimer(self)
        self.time_label = QLabel("00:00:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("StopWatch")
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        
        self.setLayout(vbox)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        
        vbox.addLayout(hbox)
        
        
        self.time_label.setAlignment(Qt.AlignCenter)
        
        self.start_button.setObjectName("start_button")
        self.stop_button.setObjectName("stop_button")
        self.reset_button.setObjectName("reset_button")
        
        self.setStyleSheet("""
                           QPushButton, QLabel{
                               padding : 15px 40px;
                               margin : 25px;
                               font-weight : bold;
                               font-family : calibri;
                           }
                           QPushButton{
                               font-size : 25px;
                               border-radius : 20px; 
                           }
                           QPushButton#start_button{
                               background-color : hsl(151, 96%, 67%);
                               
                           }
                           QPushButton#stop_button{
                               background-color : hsl(63, 96%, 67%);
                               
                           }
                           QPushButton#reset_button{
                               background-color : hsl(354, 96%, 67%);
                               
                           }
                           QLabel{
                               font-size : 100px;
                               background-color : #03fcfc;
                               border-radius : 24px;
                           }
                           
        """)
        
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)
        
        
    def start(self):
        self.timer.start(10)
    
    
    def stop(self):
        self.timer.stop()
    
    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))
        
    
    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
    
    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())

