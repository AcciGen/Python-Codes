def __init__(self):
		super().__init__()
		self.show()
		self.setFixedSize(520, 500)
		self.setWindowTitle("Tic Tac Toe")
		self.setWindowIcon(QIcon("C:\\Codes\\PyCodes\\PyQt6\\Tic Tac Toe.ico"))
		self.setStyleSheet("background: black; color: lime; font-size: 20px")