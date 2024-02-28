from PySide6 import QtWidgets, QtCore

class WelcomeScreen(QtWidgets.QWidget):
    startSelect = QtCore.Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        layout = QtWidgets.QVBoxLayout()

        welcomeLabel = QtWidgets.QLabel("Welcome to the Quiz Game!", alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(welcomeLabel)

        startButton = QtWidgets.QPushButton("Start Quiz")
        startButton.clicked.connect(self.emitStart)
        layout.addWidget(startButton)

        self.setLayout(layout)

    def emitStart(self):
        self.startSelect.emit("start")



