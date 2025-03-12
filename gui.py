
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QVBoxLayout, QTextEdit, QPushButton, QLabel, QLineEdit, QComboBox, QHBoxLayout, QGridLayout, QWidget
from actions import Actions

"""
Create search functionality that searches for customer name in a thread and refreshes the search every second.
If no customer found then can add new customer.
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.actions = Actions(self)
        self.initUI()

    def initUI(self):
        """
        Initializes the UI layout.
        """
        self.setWindowTitle('Customer Database')
        self.setGeometry(100, 100, 800, 600)

        # Create the main layout
        mainLayout = QHBoxLayout()
        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

        # Create the sub-layout columns
        leftLayout = QVBoxLayout()
        rightLayout = QVBoxLayout()

        # Create the group boxes
        self.createMessageLogGroupBox()
        self.createSearchGroupbox()

        # Add the group boxes to the sub-layout columns
        leftLayout.addWidget(self.messageLogGroupBox)
        rightLayout.addWidget(self.searchCustomerGroupBox)

        # Add the sub-layout columns to the main layout
        mainLayout.addLayout(leftLayout)
        mainLayout.addLayout(rightLayout)

#region Message Log
    def createMessageLogGroupBox(self):
        """
        Creates the message log group box.
        """
        self.messageLogGroupBox = QGroupBox("Message Log", self)
        
        messageLogLayout = QVBoxLayout()
        self.messageLog = QTextEdit()
        self.messageLog.setReadOnly(True)
        messageLogLayout.addWidget(self.messageLog)
        
        self.clearButton = QPushButton("Clear", self)
        messageLogLayout.addWidget(self.clearButton)
        self.clearButton.clicked.connect(self.messageLog.clear)
        
        self.messageLogGroupBox.setLayout(messageLogLayout)
#endregion Message Log

    def createSearchGroupbox(self):
        """
        Creates the search groupbox.
        """
        self.searchCustomerGroupBox = QGroupBox("Customer Search")

        customerNameLayout = QHBoxLayout()
        self.firstNameLabel = QLabel("First Name: ", self)
        customerNameLayout.addWidget(self.firstNameLabel)

        

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
