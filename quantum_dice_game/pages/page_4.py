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
from ..engines.resource_path import *

def build_state4():
    w = QWidget()
    layout = QVBoxLayout()

    # === Heading ===
    heading = QLabel("<h1>Observing Wave Function Collapse</h1>")
    heading.setAlignment(Qt.AlignHCenter)
    heading.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
    layout.addWidget(heading)

    # === Run Button ===
    run_button = QPushButton("Generate Visual (May take a while)")
    run_button.setFixedSize(400, 40)
    run_button.setStyleSheet("""
        QPushButton {
            background-color: #98FB98;
            font-size: 14px;
            font-weight: bold;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #3CB371;
            color: white;
        }
    """)
    layout.addWidget(run_button, alignment=Qt.AlignHCenter)

    # === Bullet Points ===
    # bullets = [
    #     "• Before a quantum system is measured, all possible states exist with certain probabilities.",
    #     "• When a measurement occurs, the system is forced to 'choose' one of those possible outcomes.",
    #     "    • The higher the probability of a state, the more likely it is to be selected.",
    #     "• Once a choice is made, the probabilities collapse.",
    #     "    • The selected state now has a probability of 1.",
    #     "    • All other states drop to a probability of 0.",
    #     "• This phenomenon is known as 'Wave Function Collapse'.",
    #     "• It represents the transition from the quantum world to the classical world — where we observe only one outcome."
    # ]
    bullets = page_4_1_bullets()

    for b in bullets:
        label = QLabel(b)
        label.setAlignment(Qt.AlignLeft)
        layout.addWidget(label)


    # === GIF Player ===
    gif_label = QLabel()
    gif_label.setFixedSize(400, 300)
    gif_label.setAlignment(Qt.AlignCenter)
    gif_label.setStyleSheet("border: 1px dashed #ccc; padding: 10px;")
    gif_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    gif_container = QHBoxLayout()
    gif_container.addStretch()
    gif_container.addWidget(gif_label)
    gif_container.addStretch()
    layout.addLayout(gif_container)

    # === Click Logic ===
    def run_and_display_circuit():
        try:
            # Load count results from file
            with open(quantum_circuit_counts_pkl(), 'rb') as f:
                counts = pickle.load(f)

            # Determine most selected state and create animation
            selected = returnSelectedState(counts)
            createAnimation(selected)

            # Display the GIF
            gif_path = wf_collapse_gif_path()
            if os.path.exists(gif_path):
                movie = QMovie(gif_path)
                
                # Force it to scale to the label size
                movie.setScaledSize(gif_label.size())

                gif_label.setMovie(movie)
                movie.start()
            else:
                gif_label.setText("GIF not found.")

        except Exception as e:
            print("Error:", e)
            gif_label.setText("An error occurred while processing.")

        # === Bullet Points ===
        bullets = [
            f"• In our case, state {selected} was chosen"
        ]
        # bullets = 
        for b in bullets:
            label = QLabel(b)
            label.setAlignment(Qt.AlignLeft)
            layout.addWidget(label)

    run_button.clicked.connect(run_and_display_circuit)

    

    # === Final Layout Stretch ===
    layout.addStretch()
    w.setLayout(layout)
    return w
