import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class ResinByteApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle('ResinByte')

        # Set the size of the window
        self.setGeometry(100, 100, 800, 600)

        # Create a vertical layout
        layout = QVBoxLayout()

        # Create a label for the company name banner
        self.banner = QLabel('ResinByte', self)
        
        # Add the banner to the layout
        layout.addWidget(self.banner)
        # Create a horizontal line (QFrame)
        line = QFrame()

        # Add the horizontal line to the layout
        layout.addWidget(line)

        # Set the layout for the main window
        self.setLayout(layout)

if __name__ == '__main__':
    # Create the application instance
    app = QApplication(sys.argv)

    with open("main.qss", "r") as file:
        app.setStyleSheet(file.read())

    # Set the application name
    app.setApplicationName('ResinByte')

    # Create the main window instance
    window = ResinByteApp()
    
    # Show the window
    window.show()

    # Execute the application
    sys.exit(app.exec_())
