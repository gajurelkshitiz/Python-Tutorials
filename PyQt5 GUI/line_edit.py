import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 200, 700, 500)
        self.line_edit = QLineEdit(self)
        self.push_button = QPushButton("Submit", self)
        
        
        self.initUI()
        
    
    def initUI(self):
        self.line_edit.setGeometry(10, 10, 350, 50)
        self.line_edit.setStyleSheet("font-size: 30px;"
                                     "font-style: Arial;")
        self.push_button.setGeometry(360, 20, 100, 40)
        self.push_button.setStyleSheet("font-size: 20px;"
                                     "font-style: Arial;")
        
        self.line_edit.setPlaceholderText("Enter Your Name:")
        
        self.push_button.clicked.connect(self.submitted)
        
    
    def submitted(self):
        text = self.line_edit.text()
        print(f"Hello {text}")
        
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())