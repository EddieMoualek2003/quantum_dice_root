from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from ..engines.backend_engine import createCircuit
from ..engines.resource_path import quantum_circuit_image, quantum_circuit_pkl
import os
import pickle

def build_state2():
    w = QWidget()
    layout = QVBoxLayout()

    # Heading
    heading = QLabel("<h1>Quantum Circuit Runner</h1>")
    heading.setAlignment(Qt.AlignHCenter)
    heading.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
    layout.addWidget(heading)

    # Run button (centered under heading)
    run_button = QPushButton("Create Quantum Circuit")
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

    # Bullets (left-aligned)
    bullets = [
        "• In this stage, we’ll create and run a quantum circuit.",
        "• Superposition is achieved by applying Hadamard gates to individual qubits.",
        "• This should (in theory) give each state an equal chance of being measured.",
        "• However, due to noise or hardware imperfections, results may vary.",
        "• Let’s first take a look at the quantum circuit for a 3-qubit superposition..."
    ]

    for b in bullets:
        label = QLabel(b)
        label.setAlignment(Qt.AlignLeft)
        layout.addWidget(label)

    # Output image area — centered in its own container
    circuit_output = QLabel()
    circuit_output.setFixedSize(400, 300)
    circuit_output.setAlignment(Qt.AlignCenter)
    circuit_output.setStyleSheet("border: 1px dashed #ccc; padding: 10px;")
    circuit_output.setScaledContents(True)

    image_container = QHBoxLayout()
    image_container.addStretch()
    image_container.addWidget(circuit_output)
    image_container.addStretch()
    layout.addLayout(image_container)

    # Click logic
    def run_and_display_circuit():
        ## Create quantum circuit.
        qc = createCircuit()

        ## Save it as a pickle object
        with open(quantum_circuit_pkl(), 'wb') as f:
            pickle.dump(qc, f)

        ## Load the saved image
        filename = quantum_circuit_image() # This is the file path for the quantum circuit image.
        if os.path.exists(filename):
            pixmap = QPixmap(filename)
            circuit_output.setPixmap(pixmap)
        else:
            circuit_output.setText("Failed to generate circuit image.")

    run_button.clicked.connect(run_and_display_circuit)

    layout.addStretch()
    w.setLayout(layout)
    return w
