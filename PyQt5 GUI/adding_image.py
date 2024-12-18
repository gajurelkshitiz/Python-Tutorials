import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 100, 1000, 800)
        
        label = QLabel(self)
        label.setGeometry(0, 0, 400, 550)
        
        pixmap = QPixmap("D:\\Downloads\\93a2a27a-48df-4ee6-9b33-a94a382b4d0b.jpg")
        label.setPixmap(pixmap)
        
        label.setScaledContents(True)
        
        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) // 2, 
                          label.width(), 
                          label.height())
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
        