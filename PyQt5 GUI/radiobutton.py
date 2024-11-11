import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup, QLabel, QWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 200, 700, 500)
        
        self.label1 = QLabel("Payment Type:", self)
        self.radio1 = QRadioButton("MasterCard", self)
        self.radio2 = QRadioButton("Visa Card", self)
        self.radio3 = QRadioButton("Debit Card", self)
        self.label2 = QLabel("Payment Options:", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)
        
        self.radio_button1 = QButtonGroup(self)
        self.radio_button2 = QButtonGroup(self)
        
        self.initUI()
        
    
    def initUI(self):
        
        self.label1.setGeometry(0, 0, 400, 100)
        self.radio1.setGeometry(10, 100, 300, 50)
        self.radio2.setGeometry(10, 150, 300, 50)
        self.radio3.setGeometry(10, 200, 300, 50)
        self.label2.setGeometry(0, 250, 400, 100)
        self.radio4.setGeometry(10, 350, 300, 50)
        self.radio5.setGeometry(10, 400, 300, 50)
        
        # self.radio1.setStyleSheet("font-size : 30px;")
        # self.radio2.setStyleSheet("font-size : 30px;")
        # self.radio3.setStyleSheet("font-size : 30px;")
        

        # Instead of above we will set-style at once.
        self.setStyleSheet("QRadioButton{"
                           "font-size : 30px;"
                           "font-family : Arial;"
                           "padding : 10px"
                           "}"
                           
                           "QLabel{"
                           "font-size : 40px;"
                           "font-family : Arial;"
                           "}")
        
        
        
        self.radio_button1.addButton(self.radio1)
        self.radio_button1.addButton(self.radio2)
        self.radio_button1.addButton(self.radio3)
        self.radio_button2.addButton(self.radio4)
        self.radio_button2.addButton(self.radio5)
        
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)
        
    
    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected.")
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())