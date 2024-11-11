import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        
        self.initUI()
        
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        hbox = QHBoxLayout()
        
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        
        central_widget.setLayout(hbox)
        
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
        
        self.setStyleSheet("""
                QPushButton{
                    font-size : 25px;
                    font-family : Arial;
                    padding : 15px 55px;
                    margin : 20px;
                    border : 3px solid;
                    border-radius : 12px
                }
                QPushButton#button1{
                    background-color : red;
                }   
                QPushButton#button2{
                    background-color : yellow;
                }
                QPushButton#button3{
                    background-color : green;
                }  
                QPushButton#button1:hover{
                    font-size : 30px;
                }   
                QPushButton#button2:hover{
                    font-size : 30px;
                }
                QPushButton#button3:hover{
                    font-size : 30px;
                }          
                        
        """)
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())