from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QSizePolicy,
    QLineEdit, QPushButton, QHBoxLayout
)
from PyQt5.QtCore import Qt

# from custom_widgets import RainbowButton  # or wherever you saved it
# from custom_widgets import GradientRainbowButton
from ..engines.custom_widgets import AnimatedGradientButton
def build_login(on_continue_callback):
    w = QWidget()
    layout = QVBoxLayout()
    layout.setSpacing(15)

    # Heading
    heading = QLabel("<h1>Welcome to Schrödinger's Dice Game</h1>")
    heading.setAlignment(Qt.AlignHCenter)
    heading.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
    layout.addWidget(heading)

    # Subheading
    subheading = QLabel("Unlock the power of Watson to enhance your quantum journey.")
    subheading.setAlignment(Qt.AlignHCenter)
    subheading.setWordWrap(True)
    layout.addWidget(subheading)

    # API Key Input
    api_key_input = QLineEdit()
    api_key_input.setPlaceholderText("Enter your IBM API Key")
    api_key_input.setEchoMode(QLineEdit.Password)
    layout.addWidget(api_key_input)

    # Project ID Input
    project_id_input = QLineEdit()
    project_id_input.setPlaceholderText("Enter your Watson Project ID")
    layout.addWidget(project_id_input)

    # Buttons
    button_layout = QVBoxLayout()

    login_button = AnimatedGradientButton("Login and Unlock the Power of Watson")
    login_button.setStyleSheet("font-weight: bold; padding: 10px;")

    skip_button = QPushButton("Skip Watson Sign-In")
    skip_button.setStyleSheet("""
        QPushButton {
            color: gray;
            background-color: #f0f0f0;
            border: none;
            font-size: 10pt;
        }
        QPushButton:hover {
            text-decoration: underline;
            color: #555;
        }
    """)

    # Connect both buttons to callback
    login_button.clicked.connect(lambda: on_continue_callback(use_watson=True))
    skip_button.clicked.connect(lambda: on_continue_callback(use_watson=False))

    button_layout.addWidget(login_button)
    button_layout.addWidget(skip_button, alignment=Qt.AlignHCenter)

    layout.addLayout(button_layout)
    layout.addStretch()
    w.setLayout(layout)

    return w, api_key_input, project_id_input, login_button, skip_button
