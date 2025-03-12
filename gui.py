import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QVBoxLayout, QTextEdit, QPushButton, QLabel, QLineEdit, QComboBox, QHBoxLayout, QGridLayout, QWidget
from actions import Actions

"""
Defines the main UI for the customer database.
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.actions = Actions(self)
        self.initUI()

#region GUI Layout
    def initUI(self):
        """
        Initializes the GUI layout.
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
        self.createEnterModelGroupBox()
        self.createRunTestGroupBox()
        
        # Add the group boxes to the sub-layout columns
        leftLayout.addWidget(self.messageLogGroupBox)
        rightLayout.addWidget(self.enterModelGroupBox)
        rightLayout.addWidget(self.runTestGroupBox)
        
        # Add the sub-layout columns to the main layout
        mainLayout.addLayout(leftLayout)
        mainLayout.addLayout(rightLayout)

        self.modelComboBox.currentIndexChanged.connect(self.actions.updateEnterModelButtonState)
        self.actions.updateEnterModelButtonState()  # Initial check

        self.modelComboBox.currentIndexChanged.connect(self.actions.updateFrequencyInputState)
        self.actions.updateFrequencyInputState()  # Initial check
#endregion GUI Layout

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


#region Enter Model
    def createEnterModelGroupBox(self):
        """
        Creates the Enter Model group box.
        """
        self.enterModelGroupBox = QGroupBox("Enter Model", self)
        
        enterModelLayout = QHBoxLayout()
        self.amplitude = QLabel("Model Name:", self)
        enterModelLayout.addWidget(self.amplitude)
        
        self.modelComboBox = QComboBox(self)
        self.modelComboBox.addItems(MODELS)
        enterModelLayout.addWidget(self.modelComboBox)
        
        self.inputFrequency = QLineEdit(self)
        self.inputFrequency.setPlaceholderText("Enter Frequency")
        enterModelLayout.addWidget(self.inputFrequency)

        self.crystalType = QLineEdit(self)
        self.crystalType.setPlaceholderText("Enter Crystal Type")
        enterModelLayout.addWidget(self.crystalType)

        self.enterModelButton = QPushButton("Enter Model", self)
        enterModelLayout.addWidget(self.enterModelButton)
        self.enterModelButton.clicked.connect(self.actions.enterModel)
        
        self.enterModelGroupBox.setLayout(enterModelLayout)
#endregion Enter Model

#region Run Test
    def createRunTestGroupBox(self):
        """
        Creates the Run Test group box.
        """
        self.runTestGroupBox = QGroupBox("Run Test", self)
        
        runTestLayout = QGridLayout()
        
        # Setup Test Equipment Button in its own horizontal layout
        setupEquipmentLayout = QHBoxLayout()
        self.setupEquipmentButton = QPushButton("Setup Test Equipment", self)
        self.setupEquipmentButton.setEnabled(False)
        self.setupEquipmentButton.clicked.connect(self.actions.setupTestEquipment)
        setupEquipmentLayout.addWidget(self.setupEquipmentButton)
        runTestLayout.addLayout(setupEquipmentLayout, 0, 0, 1, 2)
        
        # Modulation Amplitude
        self.amplitude = QLabel("Modulation Amplitude", self)
        runTestLayout.addWidget(self.amplitude, 1, 0)
        self.amplitudeInput = QLineEdit(self)
        self.amplitudeInput.setPlaceholderText("Measure Modulation Amplitude")
        self.amplitudeInput.setEnabled(False)
        runTestLayout.addWidget(self.amplitudeInput, 1, 1)
        self.amplitudeButton = QPushButton("Acquire", self)
        self.amplitudeButton.setEnabled(False)
        runTestLayout.addWidget(self.amplitudeButton, 1, 2)
        self.amplitudeButton.clicked.connect(self.actions.toggleAmplitudeThread)

        # Upper Rail
        self.upperRail = QLabel("Upper Rail", self)
        runTestLayout.addWidget(self.upperRail, 2, 0)
        self.upperRailInput = QLineEdit(self)
        self.upperRailInput.setPlaceholderText("Measure Upper Rail")
        self.upperRailInput.setEnabled(False)
        runTestLayout.addWidget(self.upperRailInput, 2, 1)
        self.upperRailButton = QPushButton("Acquire", self)
        self.upperRailButton.setEnabled(False)
        runTestLayout.addWidget(self.upperRailButton, 2, 2)
        self.upperRailButton.clicked.connect(self.actions.toggleUpperRailThread)

        # Lower Rail
        self.lowerRail = QLabel("Lower Rail", self)
        runTestLayout.addWidget(self.lowerRail, 3, 0)
        self.lowerRailInput = QLineEdit(self)
        self.lowerRailInput.setPlaceholderText("Measure Lower Rail")
        self.lowerRailInput.setEnabled(False)
        runTestLayout.addWidget(self.lowerRailInput, 3, 1)
        self.lowerRailButton = QPushButton("Acquire", self)
        self.lowerRailButton.setEnabled(False)
        runTestLayout.addWidget(self.lowerRailButton, 3, 2)
        self.lowerRailButton.clicked.connect(self.actions.toggleLowerRailThread)

        # Dark Level
        self.darkLevel = QLabel("Dark Level", self)
        runTestLayout.addWidget(self.darkLevel, 4, 0)
        self.darkLevelInput = QLineEdit(self)
        self.darkLevelInput.setPlaceholderText("Measure Dark Level")
        self.darkLevelInput.setEnabled(False)
        runTestLayout.addWidget(self.darkLevelInput, 4, 1)
        self.darkLevelButton = QPushButton("Acquire", self)
        self.darkLevelButton.setEnabled(False)
        runTestLayout.addWidget(self.darkLevelButton, 4, 2)
        self.darkLevelButton.clicked.connect(self.actions.toggleDarkLevelThread)

        self.runTestGroupBox.setLayout(runTestLayout)

#endregion Run Test

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())