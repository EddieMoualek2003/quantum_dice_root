from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSizePolicy,
    QTableWidget, QTableWidgetItem
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from ..engines.backend_engine import *
from ..engines.resource_path import *
import os
import pickle

def build_state3():
    w = QWidget()
    layout = QVBoxLayout()

    # Heading
    heading = QLabel("<h1>Quantum Circuit Results</h1>")
    heading.setAlignment(Qt.AlignHCenter)
    heading.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
    layout.addWidget(heading)

    # Run button
    run_button = QPushButton("Run Quantum Circuit")
    run_button.setFixedSize(200, 40)
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

    # Bullets
    bullets = [
        "• You've now seen what a quantum circuit looks like.",
        "• Now, we'll run and measure it — forcing the quantum system to select a single outcome.",
        "• In quantum computing, it's common to run the same circuit multiple times to estimate the probability distribution of all possible states.",
        "• These repetitions are called \"shots.\"",
        "• Ideally, each state should be equally likely — assuming perfect superposition and no noise.",
        "• In practice, we may observe deviations due to noise, decoherence, or gate imperfections."
    ]

    for b in bullets:
        label = QLabel(b)
        label.setAlignment(Qt.AlignLeft)
        layout.addWidget(label)

    image_container = QHBoxLayout()
    image_container.addStretch()
    image_container.addStretch()
    layout.addLayout(image_container)

    # Table (initially empty)
    table = QTableWidget()
    table.setColumnCount(3)
    table.setHorizontalHeaderLabels(["State", "Expected Count", "Actual Count"])
    layout.addWidget(table)

    # Click logic
    def run_and_display_circuit():
        with open(quantum_circuit_pkl(), 'rb') as f:
            qc = pickle.load(f)

        counts, shots = noisy_simulator(qc)
        with open(quantum_circuit_counts_pkl(), 'wb') as f:
            pickle.dump(counts, f)
        

        # Populate table
        states = sorted(counts.keys())  # consistent order
        table.setRowCount(len(states))
        expected = shots // 8  # uniform distribution for 3 qubits

        for row, state in enumerate(states):
            table.setItem(row, 0, QTableWidgetItem(state))
            table.setItem(row, 1, QTableWidgetItem(str(expected)))
            table.setItem(row, 2, QTableWidgetItem(str(counts[state])))
        
        max_state = max(counts, key=counts.get)
        max_count = counts[max_state]


        # Bullets
        bullets = [
            f"• Most frequent state: {max_state} with count: {max_count}.",
            f"• Next, we will look at wave function collapse, and see what happens when a measurement is made!"
        ]
        for b in bullets:
            label = QLabel(b)
            label.setAlignment(Qt.AlignLeft)
            layout.addWidget(label)

    run_button.clicked.connect(run_and_display_circuit)

    layout.addStretch()
    w.setLayout(layout)
    return w
