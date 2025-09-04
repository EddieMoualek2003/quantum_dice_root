from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from ..engines.generate_superposition_equations import gen_equations_combined
from ..engines.resource_path import superpos_equations
import os

def build_state1():
    # Generate the combined equation image
    out_path = superpos_equations()

    w = QWidget()
    layout = QVBoxLayout()

    # Heading
    heading = QLabel("<h1>What is Superposition?</h1>")
    heading.setAlignment(Qt.AlignHCenter)
    heading.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
    layout.addWidget(heading)

    # Bullet points
    bullets = [
        "• Superposition is a fundamental principle of quantum mechanics.",
        "• A quantum system can exist in multiple states at the same time.",
        "• A qubit can be in a combination of the |0⟩ and |1⟩ states.",
        "• This is expressed as ψ = α|0⟩ + β|1⟩, where α and β are probability amplitudes.",
        "• Upon measurement, the state collapses to either |0⟩ or |1⟩.",
        "• Examples of superposition for 1, 2, and 3-qubit systems are shown below:"
    ]

    for b in bullets:
        label = QLabel(b)
        layout.addWidget(label)

    # Image label
    equation_output = QLabel()
    equation_output.setAlignment(Qt.AlignHCenter)
    equation_output.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    equation_output.setStyleSheet("border: 1px dashed #ccc; padding: 10px;")
    layout.addWidget(equation_output)

    # Load the image from the generated path
    if os.path.exists(out_path):
        pixmap = QPixmap(out_path)
        equation_output.setPixmap(pixmap)
        equation_output.setScaledContents(True)
    else:
        equation_output.setText("Equation image not found.")

    layout.addStretch()
    w.setLayout(layout)
    return w
