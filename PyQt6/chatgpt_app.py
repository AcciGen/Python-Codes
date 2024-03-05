import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit
import openai
API_KEY = "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"
openai.api_key = API_KEY


class ChatGPT(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Chat UI')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)
        self.text_input = QLineEdit()

        layout.addWidget(self.text_display)
        layout.addWidget(self.text_input)

        self.setLayout(layout)

        self.text_input.returnPressed.connect(self.handle_input)

    def handle_input(self):
        user_input = self.text_input.text()

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=self.text_input.text(),
            max_tokens=50
        )
        self.text_input.clear()
        self.text_display.append(f"You: {user_input}")
        self.text_display.append(f"AI: {response.choices[0].text.strip()}")


app = QApplication(sys.argv)
window = ChatGPT()
window.show()
app.exec()
