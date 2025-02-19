from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QGroupBox, QTextEdit, QLineEdit
import sys

class GUI:
    def __init__(self):
        """
        Create the main window and add the layout.
        """
        app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.window.setWindowTitle('Basic PyQt5 Window')
        self.window.setGeometry(100, 100, 600, 400)
        self.layout()
        
        self.window.show()
        sys.exit(app.exec_())

    def layout(self):
        """
        Create the layout and manage the components.
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
        right_layout.addWidget(self.button_groupbox())

    def status_log_groupbox(self):
        """
        Create the groupbox for the status log.
        """
        groupbox = QGroupBox('Status Log')
        layout = QVBoxLayout()
        groupbox.setLayout(layout)

        status_log = QTextEdit()
        status_log.setReadOnly(True)
        layout.addWidget(status_log)

        return groupbox
    
    def button_groupbox(self):
        """
        Create the groupbox for the buttons.
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

        return groupbox

def main():
    gui = GUI()

if __name__ == "__main__":
    main()
