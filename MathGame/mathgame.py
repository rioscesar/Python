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

        self.hbox = QtGui.QHBoxLayout()
        self.hbox.setContentsMargins(5, 5, 5, 5)
        self.hbox.addWidget(topFiller)

        self.createAction()
        self.dif_and_operation()

        self.hbox.addWidget(self.dif)
        self.hbox.addWidget(self.op)
        self.hbox.addWidget(bottomFiller)
        widget.setLayout(self.hbox)

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

    def intermediate(self):
        self.difficulty = "INTERMEDIATE"
        self.delete_diff = True
        self.delete()

    def extreme(self):
        self.difficulty = "EXTREME"
        self.delete_diff = True
        self.delete()

    def add(self):
        self.operation = "ADDITION"
        self.delete_op = True
        self.delete()

    def sub(self):
        self.operation = "SUBTRACTION"
        self.delete_op = True
        self.delete()

    def mult(self):
        self.operation = "MULTIPLICATION"
        self.delete_op = True
        self.delete()

    def div(self):
        self.operation = "DIVISION"
        self.delete_op = True
        self.delete()

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
            d = self.hbox.takeAt(1)
            d.widget().deleteLater()
            o = self.hbox.takeAt(1)
            o.widget().deleteLater()



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
        a = str(a)
        b = str(b)

        if self.op == "ADDITION":
            self.__answer = a + b
            return a + " + " + b
        elif self.op == "SUBTRACTION":
            self.__answer = a - b
            return a + " - " + b
        elif self.op == "MULTIPLICATION":
            self.__answer = a * b
            return a + " * " + b
        else:
            self.__answer = a / b
            return a + " / " + b

    def check_answer(self, uanswer):
        if uanswer == self.__answer:
            return True
        return False


def main():
    app = QtGui.QApplication(sys.argv)
    ex = MathGame()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
