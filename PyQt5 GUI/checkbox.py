import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.checkbox = QCheckBox("Do you like food?", self)
        self.initUI()
        
    def initUI(self):
        self.checkbox.setGeometry(20, 0, 500, 80)
        self.checkbox.setStyleSheet("font-size: 30px;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_state_changed)
        
    def checkbox_state_changed(self, state):
        if state == Qt.Checked:
            print("You liked food.")
        else:
            print("You DO NOT like food.")
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())