from dotenv import load_dotenv
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from talk_to_google_sheets import TalkToGoogleSheets
from talk_to_openai import fetch_openai_response


class MoneyBoyApp(QMainWindow):
    def __init__(self, sheet_client):
        super().__init__()

        self.sheet_client = sheet_client
        self.init_ui()

    def init_ui(self):
        # Set up the main window
        self.setWindowTitle("Money Boy Assistant")
        self.setMinimumSize(600, 400)

        # Central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = self.make_window(central_widget)

        # Heading
        main_layout.addWidget(self.make_heading())

        # Input row
        input_layout = QHBoxLayout()
        input_layout.setSpacing(10)

        query_label = QLabel("Enter your query:")
        query_font = QFont("Segoe UI", 11)
        query_label.setFont(query_font)
        input_layout.addWidget(query_label)

        self.query_edit = QLineEdit()
        self.query_edit.setPlaceholderText("Type your question here...")
        self.query_edit.setFont(query_font)
        input_layout.addWidget(self.query_edit)

        ask_button = QPushButton("Ask")
        ask_button.setFont(QFont("Segoe UI", 11, QFont.Bold))
        ask_button.clicked.connect(self.run_query)
        input_layout.addWidget(ask_button)

        main_layout.addLayout(input_layout)

        # Response text area
        self.response_text = QTextEdit()
        self.response_text.setFont(query_font)
        self.response_text.setReadOnly(True)
        main_layout.addWidget(self.response_text)

        # Clear button row
        main_layout.addLayout(self.make_clear_button())

    def make_window(self, central_widget):
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        return layout

    def make_heading(self):
        heading_label = QLabel("Money Boy Assistant")
        heading_font = QFont("Segoe UI", 20, QFont.Bold)
        heading_label.setFont(heading_font)
        heading_label.setAlignment(Qt.AlignCenter)
        return heading_label

    def make_clear_button(self):
        clear_layout = QHBoxLayout()
        clear_layout.addStretch()
        clear_button = QPushButton("Clear")
        clear_button.setFont(QFont("Segoe UI", 11, QFont.Bold))
        clear_button.clicked.connect(self.clear_response)
        clear_layout.addWidget(clear_button)
        return clear_layout

    def run_query(self):
        user_query = self.query_edit.text().strip()
        if not user_query:
            self.set_response("Please enter a query.")
            return

        try:
            data = self.sheet_client.get_all_data()
            response = fetch_openai_response(data, user_query)
            self.set_response(response)
        except Exception as e:
            self.set_response(f"An error occurred: {e}")

    def set_response(self, text):
        self.response_text.setPlainText(text)

    def clear_response(self):
        self.response_text.clear()
        self.query_edit.clear()

def run():
    load_dotenv()
    sheet_client = TalkToGoogleSheets()
    app = QApplication([])
    window = MoneyBoyApp(sheet_client)

    window.show()
    app.exec()

if __name__ == "__main__":
    run()
