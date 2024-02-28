from PySide6 import QtWidgets, QtCore

class QuestionScreen(QtWidgets.QWidget):
    answerSelected = QtCore.Signal(str)

    def __init__(self, question, answers):
        super().__init__()
        self.question = question
        self.answers = answers
        self.setupUi()

    def setupUi(self):
        layout = QtWidgets.QVBoxLayout()

        questionLabel = QtWidgets.QLabel(self.question, alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(questionLabel)

        for answer in self.answers:
            btn = QtWidgets.QPushButton(answer)
            btn.clicked.connect(self.emitAnswer)
            layout.addWidget(btn)

        self.setLayout(layout)

    def emitAnswer(self):
        clickedButton = self.sender()
        self.answerSelected.emit(clickedButton.text())
