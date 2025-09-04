from PyQt5.QtCore import Qt, QVariantAnimation
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy
from PyQt5.QtCore import Qt

def build_state0():
    w = QWidget()
    layout = QVBoxLayout()

    heading = QLabel("<h1>Welcome to Schrödinger's Dice Game</h1>")
    heading.setAlignment(Qt.AlignHCenter)
    heading.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
    layout.addWidget(heading, alignment=Qt.AlignHCenter)

    subheading = QLabel("<h2>Learning Objectives</h2>")
    subheading.setAlignment(Qt.AlignLeft)
    subheading.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
    layout.addWidget(subheading, alignment=Qt.AlignLeft)

    bullets = [
        "• Understand the concept of superposition.",
        "• Learn how superposition is created in quantum systems.",
        "• Explore the difference between theoretical predictions and actual measurements.",
        "• Observe the phenomenon of wave function collapse."
    ]

    for b in bullets:
        label = QLabel(b)
        layout.addWidget(label)

    watson_prompt = QLabel("<h3>If you need more assistance, ask WatsonX!</h3>")
    watson_prompt.setAlignment(Qt.AlignHCenter)
    watson_prompt.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
    layout.addWidget(watson_prompt, alignment=Qt.AlignHCenter)

    layout.addStretch()
    w.setLayout(layout)
    return w
