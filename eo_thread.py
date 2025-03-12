from PyQt5.QtCore import QThread, pyqtSignal
import random
import time

#region Setup Equipment Thread
class SetupEquipmentThread(QThread):
    def __init__(self, modelText, actions):
        super().__init__()
        self.modelText = modelText
        self.actions = actions
        self.running = True  # Initialize running attribute

    def run(self):
        self.actions.sendMessageToLog(f'Setting up test equipment for {self.modelText}...')
        self.actions.sendMessageToLog('Test equipment setup complete.')

    def stop(self):
        self.running = False
        self.wait()  # Ensure the thread has finished
        # Add any additional setup logic here
#endregion Setup Equipment Thread

#region Amplitude Thread
class AmplitudeThread(QThread):
    updateAmplitude = pyqtSignal(int)

    def __init__(self, amplitudeInput):
        super().__init__()
        self.amplitudeInput = amplitudeInput
        self.running = True
        self.updateAmplitude.connect(self.updateAmplitudeInput)

    def run(self):
        main_window = self.amplitudeInput.window()
        main_window.upperRailButton.setEnabled(False)
        main_window.lowerRailButton.setEnabled(False)
        main_window.darkLevelButton.setEnabled(False)
        while self.running:
            number = random.randint(0, 1000)
            self.updateAmplitude.emit(number)
            time.sleep(1)
        main_window.upperRailButton.setEnabled(True)
        main_window.lowerRailButton.setEnabled(True)
        main_window.darkLevelButton.setEnabled(True)

    def stop(self):
        self.running = False
        self.wait()  # Ensure the thread has finished

    def updateAmplitudeInput(self, number):
        current_value = self.amplitudeInput.text()
        if not current_value or number > int(current_value):
            self.amplitudeInput.setText(str(number))
#endregion Amplitude Thread

#region Upper Rail Thread
class UpperRailThread(QThread):
    updateUpperRail = pyqtSignal(int)

    def __init__(self, upperRailInput):
        super().__init__()
        self.upperRailInput = upperRailInput
        self.running = True
        self.updateUpperRail.connect(self.updateUpperRailInput)

    def run(self):
        main_window = self.upperRailInput.window()
        main_window.amplitudeButton.setEnabled(False)
        main_window.lowerRailButton.setEnabled(False)
        main_window.darkLevelButton.setEnabled(False)
        while self.running:
            number = random.randint(0, 1000)
            self.updateUpperRail.emit(number)
            time.sleep(1)
        main_window.amplitudeButton.setEnabled(True)
        main_window.lowerRailButton.setEnabled(True)
        main_window.darkLevelButton.setEnabled(True)

    def stop(self):
        self.running = False
        self.wait()  # Ensure the thread has finished

    def updateUpperRailInput(self, number):
        current_value = self.upperRailInput.text()
        if not current_value or number > int(current_value):
            self.upperRailInput.setText(str(number))
#endregion Upper Rail Thread

#region Lower Rail Thread
class LowerRailThread(QThread):
    updateLowerRail = pyqtSignal(int)

    def __init__(self, lowerRailInput):
        super().__init__()
        self.lowerRailInput = lowerRailInput
        self.running = True
        self.updateLowerRail.connect(self.updateLowerRailInput)

    def run(self):
        main_window = self.lowerRailInput.window()
        main_window.amplitudeButton.setEnabled(False)
        main_window.upperRailButton.setEnabled(False)
        main_window.darkLevelButton.setEnabled(False)
        while self.running:
            number = random.randint(0, 1000)
            self.updateLowerRail.emit(number)
            time.sleep(1)
        main_window.amplitudeButton.setEnabled(True)
        main_window.upperRailButton.setEnabled(True)
        main_window.darkLevelButton.setEnabled(True)

    def stop(self):
        self.running = False
        self.wait()  # Ensure the thread has finished

    def updateLowerRailInput(self, number):
        current_value = self.lowerRailInput.text()
        if not current_value or number < int(current_value):
            self.lowerRailInput.setText(str(number))
#endregion Lower Rail Thread

#region Dark Level Thread
class DarkLevelThread(QThread):
    updateDarkLevel = pyqtSignal(int)

    def __init__(self, darkLevelInput):
        super().__init__()
        self.darkLevelInput = darkLevelInput
        self.running = True
        self.updateDarkLevel.connect(self.updateDarkLevelInput)
        self.values = []

    def run(self):
        main_window = self.darkLevelInput.window()
        main_window.amplitudeButton.setEnabled(False)
        main_window.upperRailButton.setEnabled(False)
        main_window.lowerRailButton.setEnabled(False)
        while self.running:
            number = random.randint(-5, 5)
            self.updateDarkLevel.emit(number)
            time.sleep(1)
        main_window.amplitudeButton.setEnabled(True)
        main_window.upperRailButton.setEnabled(True)
        main_window.lowerRailButton.setEnabled(True)

    def stop(self):
        self.running = False
        self.wait()  # Ensure the thread has finished

    def updateDarkLevelInput(self, number):
        if len(self.values) >= 10:
            self.values.pop(0)
        self.values.append(number)
        average_value = sum(self.values) / len(self.values)
        self.darkLevelInput.setText(str(average_value))
#endregion Dark Level Thread