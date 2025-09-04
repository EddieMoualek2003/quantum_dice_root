import sys
import os
import shutil  # Add this import at the top of your file

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QStackedWidget, QLineEdit, QMessageBox, QTextEdit
)
from PyQt5.QtCore import Qt, QVariantAnimation
from PyQt5.QtGui import QColor
from .engines.ai_engine import *
from .pages.login_page import build_login
from .pages.page_0 import build_state0
from .pages.page_1 import build_state1
from .pages.page_2 import build_state2
from .pages.page_3 import build_state3
from .pages.page_4 import build_state4
from .pages.page_5 import build_state5


# def cleanup_gif():
#     GIF_PATH = "resource_folder_gen/schrodinger_dice_wavefunction_collapse.gif"
#     """Delete the generated GIF when the program exits."""
#     try:
#         if os.path.exists(GIF_PATH):
#             os.remove(GIF_PATH)
#             print(f"[INFO] Deleted temporary file: {GIF_PATH}")
#     except Exception as e:
#         print(f"[WARNING] Failed to delete GIF: {e}")

class ColorFadeButton(QPushButton):
    def __init__(self, text, start_color, end_color):
        super().__init__(text)
        self.start_color = QColor(start_color)
        self.end_color = QColor(end_color)
        self.current_color = self.start_color
        self.setText(text)
        self.setStyleSheet(self.build_stylesheet(self.current_color))

        self.anim = QVariantAnimation(
            self,
            startValue=self.start_color,
            endValue=self.end_color,
            duration=300,
        )
        self.anim.valueChanged.connect(self.update_color)

    def enterEvent(self, event):
        self.anim.setDirection(QVariantAnimation.Forward)
        self.anim.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.anim.setDirection(QVariantAnimation.Backward)
        self.anim.start()
        super().leaveEvent(event)

    def update_color(self, color):
        self.current_color = color
        self.setStyleSheet(self.build_stylesheet(color))

    def build_stylesheet(self, color):
        return f"""
            QPushButton {{
                background-color: {color.name()};
                color: black;
                font-weight: bold;
                font-size: 14px;
                border-radius: 5px;
                padding: 5px;
            }}
        """


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Schrödinger's Dice Game")

        self.logged_in = False
        self.current_state = 0
        self.max_state = 10

        self.keys_valid = False # Begin in the false state until keys are confirmed.

        central_widget = QWidget()
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.stack = QStackedWidget()
        self.login_page, self.api_input, self.project_input, self.login_button, self.skip_button = build_login(self.handle_login_choice)
        self.stack.addWidget(self.login_page)
        self.stack.addWidget(build_state0())
        self.stack.addWidget(build_state1())
        self.stack.addWidget(build_state2())
        self.stack.addWidget(build_state3())
        self.stack.addWidget(build_state4())
        self.stack.addWidget(build_state5())

        self.prev_btn = ColorFadeButton("Prev", "#FFB6C1", "#FF69B4")
        self.next_btn = ColorFadeButton("Next", "#ADD8E6", "#1E90FF")
        self.prev_btn.clicked.connect(self.prev_state)
        self.next_btn.clicked.connect(self.next_state)

        nav_layout = QVBoxLayout()
        nav_layout.addWidget(self.stack)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.prev_btn)
        btn_layout.addWidget(self.next_btn)
        nav_layout.addLayout(btn_layout)

        nav_widget = QWidget()
        nav_widget.setLayout(nav_layout)

        self.chatbot_panel = QWidget()
        self.chatbot_layout = QVBoxLayout()
        self.chatbot_panel.setLayout(self.chatbot_layout)

        # Replaces QLabel with QTextEdit
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setStyleSheet("background-color: #f5f5f5; padding: 5px;")
        self.chat_display.setPlaceholderText("Login to start chatting with Watson...")
        self.chatbot_layout.addWidget(self.chat_display)

        self.question_input = QLineEdit()
        self.question_input.setPlaceholderText("Type your question here...")
        self.question_input.setEnabled(False)

        self.send_button = QPushButton("Send")
        self.send_button.setEnabled(False)
        self.send_button.clicked.connect(self.send_chatbot_query)

        self.chatbot_layout.addWidget(self.question_input)
        self.chatbot_layout.addWidget(self.send_button)

        main_layout.addWidget(nav_widget, stretch=3)
        main_layout.addWidget(self.chatbot_panel, stretch=1)

        self.update_ui()

    def handle_login_choice(self, use_watson):
        self.logged_in = use_watson
        self.api_key = self.api_input.text().strip()
        self.project_id = self.project_input.text().strip()

        # If using Watson, hand over to the login processing section.
        if use_watson:
            self.login(enable_watson(self.api_key))
        else:
            QMessageBox.warning(self, "Warning", "You won't have access to WatsonX")

        print("Watson login selected:", use_watson)
        print("API Key:", self.api_key)
        print("Project ID:", self.project_id)
        self.current_state = 1
        self.stack.setCurrentIndex(self.current_state)

    def prev_state(self):
        if self.current_state > 0:
            self.current_state -= 1
        self.stack.setCurrentIndex(self.current_state)

    def next_state(self):
        if self.current_state < self.max_state - 1:
            self.current_state += 1
        self.stack.setCurrentIndex(self.current_state)

    def login(self, enable_watson_response):
        if enable_watson_response == False:
            print("Error with API Key")
            QMessageBox.critical(self, "Error", f"The key has not been accepted.")
            self.keys_valid = False
        else:
            self.keys_valid = True

        if self.keys_valid:
            self.logged_in = True
            QMessageBox.information(self, "Login", "Login successful!")
            self.activate_chatbot_interface()
        else:
            QMessageBox.warning(self, "Login", "Invalid token.")

    def activate_chatbot_interface(self):
        self.chat_display.setPlaceholderText("Ask Watson something...")
        self.question_input.setEnabled(True)
        self.send_button.setEnabled(True)

    def send_chatbot_query(self):
        question = self.question_input.text().strip()
        if not question:
            QMessageBox.information(self, "Chatbot", "Please enter a question.")
            return

        # Display the user's question
        self.chat_display.append(f"<b>You:</b> {question}")
        self.question_input.clear()

        # Generate AI response
        ai_response = ask_watson(question, self.project_id)

        # Simulated Watson response (replace with real API call if needed)
        # ai_response = f"(Simulated Watson response to: '{question}')"
        self.chat_display.append(f"<b>Watson:</b> {ai_response}")

        # Auto-scroll to bottom
        self.chat_display.verticalScrollBar().setValue(
            self.chat_display.verticalScrollBar().maximum()
        )

    def update_ui(self):
        self.stack.setCurrentIndex(self.current_state)

    def closeEvent(self, event):
        print("Game has been closed. Thanks for playing!")
        event.accept()

# if __name__ == "__main__":
def dice_gui_main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()

    exit_code = app.exec_()  # Wait until the window closes
    # window.cleanup()         # Now that the GUI has exited, cleanup is safe
    sys.exit(exit_code)

