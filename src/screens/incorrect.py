from PySide6 import QtWidgets, QtCore

class IncorrectScreen(QtWidgets.QWidget):
    nextSelect = QtCore.Signal(str)

    def __init__(self, correct):
        super().__init__()
        self.correctAnswer = correct
        self.setupUi()

    def setupUi(self):
        layout = QtWidgets.QVBoxLayout()

        incorrectLabel = QtWidgets.QLabel("Incorrect!", alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(incorrectLabel)

        answerLabel = QtWidgets.QLabel(f"The correct answer is: {self.correctAnswer}", alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(answerLabel)

        nextButton = QtWidgets.QPushButton("Next Question")
        nextButton.clicked.connect(self.emitNext)
        layout.addWidget(nextButton)

        self.setLayout(layout)

    def emitNext(self):
        self.nextSelect.emit("next")
        
