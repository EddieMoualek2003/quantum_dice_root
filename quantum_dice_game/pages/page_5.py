from PyQt5.QtWidgets import ( 
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSizePolicy,
    QTableWidget, QTableWidgetItem
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QMovie
from ..engines.backend_engine import *
import os
import pickle
from ..engines.bullets_shared import *

def build_state5():
    w = QWidget()
    layout = QVBoxLayout()

    # === Heading ===
    heading = QLabel("<h1>Well Done!</h1>")
    heading.setAlignment(Qt.AlignHCenter)
    heading.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
    layout.addWidget(heading)

    # === Bullet Points ===
    # bullets = [
    #     "• You’ve learned that quantum systems can exist in superposition — being in multiple states at once.",
    #     "• You’ve seen how circuits can be used to create and manipulate quantum states.",
    #     "• You’ve explored how measurement causes the wave function to collapse, forcing the system to choose a specific state.",
    #     "• You’ve understood that real-world quantum results may diverge from theoretical predictions due to noise and imperfections.",
    #     "• You’ve observed how probability distributions emerge through repeated measurements, or 'shots'.",
    #     "• Thank you for playing Schrödinger’s Dice Game — we hope you had fun while learning!",
    #     "• You may now close the game window whenever you're ready."
    # ]

    bullets = page_5_bullets()


    for b in bullets:
        label = QLabel(b)
        label.setAlignment(Qt.AlignLeft)
        layout.addWidget(label)
    

    # === Final Layout Stretch ===
    layout.addStretch()
    w.setLayout(layout)
    return w
