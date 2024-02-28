import sys
from PySide6 import QtWidgets
import json
from screens.welcome import WelcomeScreen
from screens.question import QuestionScreen
from screens.correct import CorrectScreen
from screens.incorrect import IncorrectScreen

class QuizApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz Game")

        with open("questions.json", 'r') as qdata:
            self.questions = json.load(qdata)
        self.currentQuestionIndex = 0

        self.initUI()

    def initUI(self):
        self.centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralWidget)

        self.showWelcome()

    def showWelcome(self):
        welcomeScreen = WelcomeScreen()
        welcomeScreen.startSelect.connect(self.showQuestion)

        self.setCentralWidget(welcomeScreen)


    def showNext(self):
        self.currentQuestionIndex += 1
        if self.currentQuestionIndex < len(self.questions):
            self.showQuestion()
        else:
            print("Quiz Complete!")

    def showQuestion(self):
        questionData = self.questions[self.currentQuestionIndex]
        self.questionScreen = QuestionScreen(questionData["question"], questionData["answers"])
        self.questionScreen.answerSelected.connect(self.handleAnswer)

        self.setCentralWidget(self.questionScreen)

    def showCorrect(self):
        correctScreen = CorrectScreen(self.questions[self.currentQuestionIndex]['correct'])
        correctScreen.nextSelect.connect(self.showNext)
        self.setCentralWidget(correctScreen)

    def showIncorrect(self):
        incorrectScreen = IncorrectScreen(self.questions[self.currentQuestionIndex]['correct'])
        incorrectScreen.nextSelect.connect(self.showNext)
        self.setCentralWidget(incorrectScreen)

    def handleAnswer(self, answer):
        if answer == self.questions[self.currentQuestionIndex]['correct']:
            self.showCorrect()
        else:
            self.showIncorrect()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    mainWindow = QuizApp()
    mainWindow.resize(400, 300)
    mainWindow.show()

    sys.exit(app.exec())
