from PyQt5.QtWidgets import QMessageBox
from eo_thread import AmplitudeThread, UpperRailThread, LowerRailThread, DarkLevelThread, SetupEquipmentThread
from eo_constants import CRYSTAL_TYPES

"""
Defines the actions that are performed in the EO test setup GUI.
Includes actions that are triggered by user interaction with buttons and functions that
update the GUI based on user input (e.g. enabling/disabling buttons, checking if input
is valid, etc.).
"""

class Actions:
    def __init__(self, main_window):
        self.main_window = main_window

#region Message Log Actions
    def sendMessageToLog(self, message):
        """
        Sends a message to the message log.
        """
        self.main_window.messageLog.append(message)

        # The 'clear' action is performed in gui.py by using python's built-in clear() method.
#endregion Message Log Actions

#region Enter Model Actions
    def updateEnterModelButtonState(self):
        """
        Enables the Enter Model button if the correct information is entered.
        """
        if self.main_window.modelComboBox.currentText() == "Select Model":
            self.main_window.enterModelButton.setEnabled(False)
        else:
            self.main_window.enterModelButton.setEnabled(True)

    def updateFrequencyInputState(self):
        """
        Disables the frequency input field if the model is NR (non-resonant).
        """
        if 'NR' in self.main_window.modelComboBox.currentText():
            self.main_window.inputFrequency.setText("N/A")
            self.main_window.inputFrequency.setEnabled(False)
        else:
            self.main_window.inputFrequency.setText("")
            self.main_window.inputFrequency.setEnabled(True)

    def checkFrequencyValid(self, frequency):
        """
        Checks if the frequency entered is valid.
        """
        try:
            freq = float(frequency)
            if freq > 0:
                return True
            else:
                self.createWarningMessageBox("Invalid Frequency: Frequency must be greater than 0.")
                return False
        except ValueError:
            self.createWarningMessageBox("Invalid Frequency: Please enter a valid number.")
            return False

    def checkCrystalValid(self, crystalType):
        """
        Checks if the crystal type entered is valid.
        """
        if crystalType in CRYSTAL_TYPES:
            return True
        else:
            self.createWarningMessageBox("Invalid Crystal Type.")
            return False

    def enterModel(self):
        """
        Gets the model info from the input fields and sends it to the message log.
        Uses checkFrequencyValid and checkCrystalValid to check if the frequency and crystal type are valid.
        """
        modelText = self.main_window.modelComboBox.currentText()
        frequency = self.main_window.inputFrequency.text()
        crystalType = self.main_window.crystalType.text()

        if 'NR' not in modelText:
            frequencyValid = self.checkFrequencyValid(frequency)
        crystalTypeValid = self.checkCrystalValid(crystalType)

        if 'NR' in modelText and crystalTypeValid:
            modelText = modelText.replace("Cx", crystalType)
        elif 'NR' not in modelText and frequencyValid and crystalTypeValid:
            modelText = modelText.replace("xx", frequency)
            modelText = modelText.replace("Cx", crystalType)
        else:
            modelText = "Invalid Model."

        self.sendMessageToLog(f'Model Entered: {modelText}')
        self.updateSetupEquipmentButtonState(modelText)
#endregion Enter Model Actions

#region Run Test Actions
    def generateRandomNumber(self):
        """
        Generates a random number between 0 and 1000.
        Used to simulate data for testing purposes.
        """
        import random
        return random.randint(0, 1000)

    def updateSetupEquipmentButtonState(self, modelText):
        """
        Enables the Setup Test Equipment button if a valid model is entered.
        Updates the button text to include the model text.
        """
        if modelText != "Invalid Model.":
            self.main_window.setupEquipmentButton.setEnabled(True)
            self.main_window.setupEquipmentButton.setText(f"Setup Test Equipment for {modelText}")
        else:
            self.main_window.setupEquipmentButton.setEnabled(False)
            self.main_window.setupEquipmentButton.setText("Setup Test Equipment")

    def setupTestEquipment(self):
        """
        Sets up the external test equipment.
        """
        buttonText = self.main_window.setupEquipmentButton.text()
        modelText = buttonText.replace("Setup Test Equipment for ", "")
        
        self.sendMessageToLog(f'Setting up test equipment for {modelText}...')
        
        # Stop any existing setup equipment thread
        if hasattr(self, 'setupEquipmentThread') and self.setupEquipmentThread.isRunning():
            self.setupEquipmentThread.stop()
            self.setupEquipmentThread = None
        
        self.setupEquipmentThread = SetupEquipmentThread(modelText, self)
        self.setupEquipmentThread.start()
        
        # Enable the buttons for acquiring amplitude, upper rail, lower rail, and dark level
        self.main_window.amplitudeButton.setEnabled(True)
        self.main_window.upperRailButton.setEnabled(True)
        self.main_window.lowerRailButton.setEnabled(True)
        self.main_window.darkLevelButton.setEnabled(True)

    def toggleAmplitudeThread(self):
        """
        Toggles the amplitude thread on and off.
        """
        if hasattr(self.main_window, 'amplitudeThread') and self.main_window.amplitudeThread is not None and self.main_window.amplitudeThread.isRunning():
            self.main_window.amplitudeThread.stop()
            self.main_window.amplitudeThread = None
            self.main_window.amplitudeButton.setText("Acquire")
            self.sendMessageToLog('Modulation Amplitude Acquired.')
        else:
            self.sendMessageToLog('Acquiring Modulation Amplitude...')
            self.main_window.amplitudeInput.clear()
            self.main_window.amplitudeThread = AmplitudeThread(self.main_window.amplitudeInput)
            self.main_window.amplitudeThread.start()
            self.main_window.amplitudeButton.setText("Stop")

    def toggleUpperRailThread(self):
        """
        Toggles the upper rail thread on and off.
        """
        if hasattr(self.main_window, 'upperRailThread') and self.main_window.upperRailThread is not None and self.main_window.upperRailThread.isRunning():
            self.main_window.upperRailThread.stop()
            self.main_window.upperRailThread = None
            self.main_window.upperRailButton.setText("Acquire")
            self.sendMessageToLog('Upper Rail Acquired.')
        else:
            self.sendMessageToLog('Acquiring Upper Rail...')
            self.main_window.upperRailInput.clear()
            self.main_window.upperRailThread = UpperRailThread(self.main_window.upperRailInput)
            self.main_window.upperRailThread.start()
            self.main_window.upperRailButton.setText("Stop")

    def toggleLowerRailThread(self):
        """
        Toggles the lower rail thread on and off.
        """
        if hasattr(self.main_window, 'lowerRailThread') and self.main_window.lowerRailThread is not None and self.main_window.lowerRailThread.isRunning():
            self.main_window.lowerRailThread.stop()
            self.main_window.lowerRailThread = None
            self.main_window.lowerRailButton.setText("Acquire")
            self.sendMessageToLog('Lower Rail Acquired.')
        else:
            self.sendMessageToLog('Acquiring Lower Rail...')
            self.main_window.lowerRailInput.clear()
            self.main_window.lowerRailThread = LowerRailThread(self.main_window.lowerRailInput)
            self.main_window.lowerRailThread.start()
            self.main_window.lowerRailButton.setText("Stop")

    def toggleDarkLevelThread(self):
        """
        Toggles the dark level thread on and off.
        """
        if hasattr(self.main_window, 'darkLevelThread') and self.main_window.darkLevelThread is not None and self.main_window.darkLevelThread.isRunning():
            self.main_window.darkLevelThread.stop()
            self.main_window.darkLevelThread = None
            self.main_window.darkLevelButton.setText("Acquire")
            self.sendMessageToLog('Dark Level Acquired.')
        else:
            self.sendMessageToLog('Acquiring Dark Level...')
            self.main_window.darkLevelInput.clear()
            self.main_window.darkLevelThread = DarkLevelThread(self.main_window.darkLevelInput)
            self.main_window.darkLevelThread.start()
            self.main_window.darkLevelButton.setText("Stop")
#endregion Run Test Actions

#region Warning Box
    def createWarningMessageBox(self, message):
        """
        Creates a warning message box.
        """
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Warning)
        messageBox.setWindowTitle("Warning")
        messageBox.setText(message)
        messageBox.exec()
#endregion Warning Box