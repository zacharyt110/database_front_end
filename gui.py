from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QGroupBox, QTextEdit, QLineEdit
import sys
from actions import Actions

class GUI:
    def __init__(self):
        """
        Create the main window and add the layout.
        """
        app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.window.setWindowTitle('Customer Database')
        self.window.setGeometry(100, 100, 600, 400)
        self.status_log = None
        self.layout()
        
        # Instantiate actions for the GUI
        self.actions = Actions(self)
        self.window.show()
        sys.exit(app.exec_())

    def layout(self):
        """
        Create the layout and manage the components.
        Calls each of the UI components to be added to the layout.
        """
        central_widget = QWidget()
        self.window.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        left_layout.addWidget(self.status_log_groupbox())
        right_layout.addWidget(self.search_database_groupbox())

    def status_log_groupbox(self):
        """
        Create the groupbox for the status log.
        """
        groupbox = QGroupBox('Status Log')
        layout = QVBoxLayout()
        groupbox.setLayout(layout)

        self.status_log = QTextEdit()
        self.status_log.setReadOnly(True)
        layout.addWidget(self.status_log)

        return groupbox

    
    def search_database_groupbox(self):
        """
        Search database groupbox.
        """
        # Main button groupbox layout
        groupbox = QGroupBox('Buttons')
        layout = QVBoxLayout()
        groupbox.setLayout(layout)

        # First row layout
        first_row = QHBoxLayout()
        layout.addLayout(first_row)
        # Create a text box
        enterFirstName = QLineEdit()
        enterFirstName.setPlaceholderText("Enter First Name")
        enterLastName = QLineEdit()
        enterLastName.setPlaceholderText("Enter Last Name")
        # Add text box to layout
        first_row.addWidget(enterFirstName)
        first_row.addWidget(enterLastName)

        # Second row layout
        second_row = QHBoxLayout()
        layout.addLayout(second_row)
        # Create a button
        search_button = QPushButton('Search')
        # Add button to layout
        second_row.addWidget(search_button)
        search_button.clicked.connect(lambda: self.actions.search_button_action(enterFirstName.text(), enterLastName.text()))

        return groupbox

    def update_status_log(self, message):
        """
        Update the status log with a new message.
        """
        self.status_log.append(message)

def main():
    gui = GUI()

if __name__ == "__main__":
    main()
