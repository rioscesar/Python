import sys
import random
from PySide import QtGui


class MathGame(QtGui.QMainWindow):
    def __init__(self):
        super(MathGame, self).__init__()
        self.delete_diff = False
        self.delete_op = False
        self.initUI()

    def initUI(self):
        # show the difficulty option along with the operations option
        # get the response and create problem

        widget = QtGui.QWidget()
        self.setCentralWidget(widget)

        topFiller = QtGui.QWidget()
        topFiller.setSizePolicy(QtGui.QSizePolicy.Expanding,
                            QtGui.QSizePolicy.Expanding)

        bottomFiller = QtGui.QWidget()
        bottomFiller.setSizePolicy(QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)

        self.layout = QtGui.QHBoxLayout()
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.layout.addWidget(topFiller)

        self.createAction()
        self.dif_and_operation()

        self.lets_play()

        self.layout.addWidget(self.dif)
        self.layout.addWidget(self.op)
        self.layout.addWidget(bottomFiller)
        widget.setLayout(self.layout)

        self.statusBar()

        self.setWindowTitle('Math Game')
        self.setMinimumSize(160, 160)
        self.resize(300, 200)

    # this method takes care of the input of the user
    def dif_and_operation(self):
        self.dif = QtGui.QPushButton('Difficulty', self)
        self.dif.move(30, 20)

        self.op = QtGui.QPushButton('Operations', self)
        self.op.move(130, 20)

        self.dif.clicked.connect(self.buttonClicked)
        self.op.clicked.connect(self.buttonClicked)

    def easy(self):
        self.difficulty = "EASY"
        self.delete_diff = True
        self.delete()
        self.lets_play()

    def intermediate(self):
        self.difficulty = "INTERMEDIATE"
        self.delete_diff = True
        self.delete()
        self.lets_play()

    def extreme(self):
        self.difficulty = "EXTREME"
        self.delete_diff = True
        self.delete()
        self.lets_play()

    def add(self):
        self.operation = "ADDITION"
        self.delete_op = True
        self.delete()
        self.lets_play()

    def sub(self):
        self.operation = "SUBTRACTION"
        self.delete_op = True
        self.delete()
        self.lets_play()

    def mult(self):
        self.operation = "MULTIPLICATION"
        self.delete_op = True
        self.delete()
        self.lets_play()

    def div(self):
        self.operation = "DIVISION"
        self.delete_op = True
        self.delete()
        self.lets_play()

    def createAction(self):
        self.EASY = QtGui.QAction("EASY", self, statusTip="Set the difficulty to EASY",
                                  triggered=self.easy)
        self.INTERMEDIATE = QtGui.QAction("INTERMEDIATE", self, statusTip="Set the difficulty to INTERMEDIATE",
                                          triggered=self.intermediate)
        self.EXTREME = QtGui.QAction("EXTREME", self, statusTip="Set the difficulty to EXTREME",
                                     triggered=self.extreme)
        self.ADDITION = QtGui.QAction("ADDITION", self, statusTip="Operation will be ADDITION",
                                      triggered=self.add)
        self.SUBTRACTION = QtGui.QAction("SUBTRACTION", self, statusTip="Operation will be SUBTRACTION",
                                         triggered=self.sub)
        self.MULTIPLICATION = QtGui.QAction("MULTIPLICATION", self, statusTip="Operation will be MULTIPLICATION",
                                            triggered=self.mult)
        self.DIVISION = QtGui.QAction("DIVISION", self, statusTip="Operation will be DIVISION",
                                      triggered=self.div)

    def buttonClicked(self):
        sender = self.sender()
        dmenu = [self.EASY, self.INTERMEDIATE, self.EXTREME]
        omenu = [self.ADDITION, self.SUBTRACTION, self.MULTIPLICATION, self.DIVISION]

        self.difmenu = QtGui.QMenu()
        for action in dmenu:
            self.difmenu.addAction(action)

        self.opmenu = QtGui.QMenu()
        for action in omenu:
            self.opmenu.addAction(action)

        if sender.text() == 'Difficulty':
            self.dif.setMenu(self.difmenu)
            self.statusBar().showMessage("Difficulty being selected")
        elif sender.text() == 'Operations':
            self.op.setMenu(self.opmenu)
            self.statusBar().showMessage("Operation being selected")
        else:
            self.statusBar().showMessage("Ready")

    def delete(self):
        if self.delete_op and self.delete_op:
            d = self.layout.takeAt(1)
            d.widget().deleteLater()
            o = self.layout.takeAt(1)
            o.widget().deleteLater()

    # timer should go here that times the user until the time runs out.
    # A tally of the number he got right should appear at the end
    def lets_play(self):
        if self.delete_op and self.delete_diff:
            self.answer = ""
            self.question = Difficulty(self.difficulty, self.operation)
            self.equation = QtGui.QLabel(self.question.equation_difficulty())
            self.input = QtGui.QLineEdit()
            self.submit = QtGui.QPushButton("SUBMIT")

            self.layout.addWidget(self.equation, 4, 8)
            self.layout.addWidget(self.input, 8)
            self.layout.addWidget(self.submit)

            self.input.textChanged.connect(self.set_answer)
            self.submit.clicked.connect(self.check)


    def set_answer(self, text):
        self.answer = text
        print(self.answer)

    def check(self):
        if self.question.check_answer(self.answer):
            print("CORRECT!")
        else:
            print("TRY AGAIN!")



class Difficulty():
    def __init__(self, dif, op):
        self.dif = dif
        self.op = op
        self.__answer = None
        random.seed()

    def equation_difficulty(self):
        if self.dif == "EASY":
            return self.create_equation(1, 10)
        elif self.dif == "INTERMEDIATE":
            return self.create_equation(10, 20)
        else:
            return self.create_equation(20, 30)

    def create_equation(self, a, b):
        a = random.randint(a, b)
        b = random.randint(a, b)

        _a = str(a)
        _b = str(b)

        if self.op == "ADDITION":
            self.__answer = a + b
            return _a + " + " + _b
        elif self.op == "SUBTRACTION":
            self.__answer = a - b
            return _a + " - " + _b
        elif self.op == "MULTIPLICATION":
            self.__answer = a * b
            return _a + " * " + _b
        else:
            self.__answer = a / b
            return _a + " / " + _b

    def check_answer(self, uanswer):
        if str(uanswer) == str(self.__answer):
            return True
        return False


def main():
    app = QtGui.QApplication(sys.argv)
    ex = MathGame()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
