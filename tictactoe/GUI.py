from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class UIHome(QWidget):
	def __init__(self,parent = None):
		super(UIHome,self).__init__(parent)
		self.title_lbl = QLabel("  TicTacToe",self)
		self.title_lbl.setGeometry(20,50,300,100)
		self.title_lbl.setFont(QFont("Times",25))
		self.play_btn = QPushButton("Play", self)
		self.play_btn.setGeometry(20,150,300,100)
		self.play_btn.setFont(QFont("Times",20))

class UIGame(QWidget):
	
	def __init__(self,parent = None):
		super(UIGame,self).__init__(parent)
 
		self.UiComponents()
		self.matrix = [[0,0,0],[0,0,0],[0,0,0]]
		self.x = 0
		

	def UiComponents(self):
		self.player = 1
		self.btn1 = QPushButton("", self)
		self.btn1.setGeometry(10, 10, 100, 100)
		self.btn1.setFont(QFont('Times', 50))
		self.btn1.clicked.connect(self.clck1)
		
		self.btn2 = QPushButton("", self)
		self.btn2.setGeometry(10, 120, 100, 100)
		self.btn2.setFont(QFont('Times', 50))
		self.btn2.clicked.connect(self.clck2)
		
		self.btn3 = QPushButton("", self)
		self.btn3.setGeometry(10, 230, 100, 100)
		self.btn3.setFont(QFont('Times', 50))
		self.btn3.clicked.connect(self.clck3)
		
		self.btn4 = QPushButton("", self)
		self.btn4.setGeometry(120, 10, 100, 100)
		self.btn4.setFont(QFont('Times', 50))
		self.btn4.clicked.connect(self.clck4)
		
		self.btn5 = QPushButton("", self)
		self.btn5.setGeometry(120, 120, 100, 100)
		self.btn5.setFont(QFont('Times', 50))
		self.btn5.clicked.connect(self.clck5)
		
		self.btn6 = QPushButton("", self)
		self.btn6.setGeometry(120, 230, 100, 100)
		self.btn6.setFont(QFont('Times', 50))
		self.btn6.clicked.connect(self.clck6)
		
		self.btn7 = QPushButton("", self)
		self.btn7.setGeometry(230, 10, 100, 100)
		self.btn7.setFont(QFont('Times', 50))
		self.btn7.clicked.connect(self.clck7)
		
		self.btn8 = QPushButton("", self)
		self.btn8.setGeometry(230, 120, 100, 100)
		self.btn8.setFont(QFont('Times', 50))
		self.btn8.clicked.connect(self.clck8)
		
		self.btn9 = QPushButton("", self)
		self.btn9.setGeometry(230, 230, 100, 100)
		self.btn9.setFont(QFont('Times', 50))
		self.btn9.clicked.connect(self.clck9)
		
		self.label = QLabel("player 1's turn",self)
		self.label.setGeometry(10,330,330,50)
		self.label.setFont(QFont('Times',15))
		
		self.restartbtn = QPushButton("restart", self)
		self.restartbtn.setGeometry(10,390,100,30)
		self.restartbtn.setFont(QFont("Times",10))
		self.restartbtn.clicked.connect(self.restart)
		
		self.homebtn = QPushButton("home", self)
		self.homebtn.setGeometry(120,390,100,30)
		self.homebtn.setFont(QFont("Times",10))
		
		self.helpbtn = QPushButton("help",self)
		self.helpbtn.setGeometry(230,390,100,30)
		self.helpbtn.setFont(QFont("Times",10))



	def clck1(self):
		self.btn1.setText("X" if self.player == 1 else "O")
		self.btn1.blockSignals(True)
		self.matrix[0][0]=self.player
		if self.test():
			self.end()
			return None
		self.label.setText("player 2's turn" if self.player == 1 else "player 1's turn")
		self.player=-self.player
	def clck2(self):
		self.btn2.setText("X" if self.player == 1 else "O")
		self.btn2.blockSignals(True)
		self.matrix[0][1]=self.player
		if self.test():
			self.end()
			return None
		self.label.setText("player 2's turn" if self.player == 1 else "player 1's turn")
		self.player=-self.player
	def clck3(self):
		self.btn3.setText("X" if self.player == 1 else "O")
		self.btn3.blockSignals(True)
		self.matrix[0][2]=self.player
		if self.test():
			self.end()
			return None
		self.label.setText("player 2's turn" if self.player == 1 else "player 1's turn")
		self.player=-self.player
	def clck4(self):
		self.btn4.setText("X" if self.player == 1 else "O")
		self.btn4.blockSignals(True)
		self.matrix[1][0]=self.player
		if self.test():
			self.end()
			return None
		self.label.setText("player 2's turn" if self.player == 1 else "player 1's turn")
		self.player=-self.player
	def clck5(self):
		self.btn5.setText("X" if self.player == 1 else "O")
		self.btn5.blockSignals(True)
		self.matrix[1][1]=self.player
		if self.test():
			self.end()
			return None
		self.label.setText("player 2's turn" if self.player == 1 else "player 1's turn")
		self.player=-self.player
	def clck6(self):
		self.btn6.setText("X" if self.player == 1 else "O")
		self.btn6.blockSignals(True)
		self.matrix[1][2]=self.player
		if self.test():
			self.end()
			return None
		self.label.setText("player 2's turn" if self.player == 1 else "player 1's turn")
		self.player=-self.player
	def clck7(self):
		self.btn7.setText("X" if self.player == 1 else "O")
		self.btn7.blockSignals(True)
		self.matrix[2][0]=self.player
		if self.test():
			self.end()
			return None
		self.label.setText("player 2's turn" if self.player == 1 else "player 1's turn")
		self.player=-self.player
	def clck8(self):
		self.btn8.setText("X" if self.player == 1 else "O")
		self.btn8.blockSignals(True)
		self.matrix[2][1]=self.player
		if self.test():
			self.end()
			return None
		self.label.setText("player 2's turn" if self.player == 1 else "player 1's turn")
		self.player=-self.player
	def clck9(self):
		self.btn9.setText("X" if self.player == 1 else "O")
		self.btn9.blockSignals(True)
		self.matrix[2][2]=self.player
		if self.test():
			self.end()
			return None
		self.label.setText("player 2's turn" if self.player == 1 else "player 1's turn")
		self.player=-self.player
	def restart(self):
		self.matrix = [[0,0,0],[0,0,0],[0,0,0]]
		self.x = 0
		self.player = 1
		self.btn1.setText("")
		self.btn2.setText("")
		self.btn3.setText("")
		self.btn4.setText("")
		self.btn5.setText("")
		self.btn6.setText("")
		self.btn7.setText("")
		self.btn8.setText("")
		self.btn9.setText("")
		self.btn1.blockSignals(False)
		self.btn2.blockSignals(False)
		self.btn3.blockSignals(False)
		self.btn4.blockSignals(False)
		self.btn5.blockSignals(False)
		self.btn6.blockSignals(False)
		self.btn7.blockSignals(False)
		self.btn8.blockSignals(False)
		self.btn9.blockSignals(False)
		self.label.setText("player 1's turn")
	
		
	def test(self):
		for i in range(3):
			if self.matrix[i][0]!=0:
				if self.matrix[i][0]==self.matrix[i][1]==self.matrix[i][2]:
					return True
		for i in range(3):
			if self.matrix[0][i]!=0:
				if self.matrix[0][i]==self.matrix[1][i]==self.matrix[2][i]:
					return True
		if self.matrix[0][0]!=0:
			if self.matrix[0][0]==self.matrix[1][1]==self.matrix[2][2]:
				return True
		if self.matrix[0][2]!=0:
			if self.matrix[0][2]==self.matrix[1][1]==self.matrix[2][0]:
				return True
		for i in range(3):
			for j in range(3):
				if self.matrix[i][j]!=0:
					self.x+=1
		if self.x < 9:
			self.x = 0
		if self.x == 9:
			return True
			
		return False
	
	def end(self):
		if self.x == 9:
			self.label.setText("It's a tie!")
		elif self.player == 1:
			self.label.setText("Player 1 wins!")
		else:
			self.label.setText("Player 2 wins!")
		self.btn1.blockSignals(True)
		self.btn2.blockSignals(True)
		self.btn3.blockSignals(True)
		self.btn4.blockSignals(True)
		self.btn5.blockSignals(True)
		self.btn6.blockSignals(True)
		self.btn7.blockSignals(True)
		self.btn8.blockSignals(True)
		self.btn9.blockSignals(True)

class UIHelp(QWidget):
	def __init__(self,parent = None):
		super(UIHelp,self).__init__(parent)
		self.rules = QLabel("Rules",self)
		self.rules.setGeometry(10,10,300,50)
		self.rules.setFont(QFont( "Times",12))
		
		self.ruleslst = QLabel("The rules are simple. All you want \nto do is get 3 X's or O's in a row. \nEither vertically, horizontally \nor diagonally.",self)
		self.ruleslst.setGeometry(10,50,310,100)
		self.ruleslst.setFont(QFont("Times",10))
		
		self.howtos = QLabel("How to play",self)
		self.howtos.setGeometry(10,150,300,50)
		self.howtos.setFont(QFont("Times",12))
		
		self.howtoslst = QLabel("In order to play, press ony of the \nbuttons without an X or O on it. \nThat will count as your turn. Then, \nthe position will be updated to \nyour sign(X or O). Keep going \nuntil you win !",self)
		self.howtoslst.setGeometry(10,190,310,150)
		self.howtoslst.setFont(QFont("Times",10))
		
		self.backbtn = QPushButton("Back", self)
		self.backbtn.setGeometry(10,350,320,50)
		self.backbtn.setFont(QFont("Times",15))

class Window(QMainWindow):
	def __init__(self,parent = None):
		super(Window,self).__init__(parent)
		self.setWindowTitle("TICTACTOE")
		self.setGeometry(100, 100, 340, 440)
		self.startUIHome()
		
	def startUIHome(self):
		self.Home = UIHome(self)
		self.setCentralWidget(self.Home)
		self.Home.play_btn.clicked.connect(self.startUIGame)
		self.show()
		
	def startUIGame(self):
		self.Game = UIGame(self)
		self.setCentralWidget(self.Game)
		self.Game.homebtn.clicked.connect(self.startUIHome)
		self.Game.helpbtn.clicked.connect(self.startUIHelp)
		self.show()
		
	def startUIHelp(self):
		self.Help = UIHelp(self)
		self.setCentralWidget(self.Help)
		self.Help.backbtn.clicked.connect(self.startUIGame)
		self.show()
    


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())