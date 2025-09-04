def page_0_bullets():
    bullets = [
        "• Understand the concept of superposition.",
        "• Learn how superposition is created in quantum systems.",
        "• Explore the difference between theoretical predictions and actual measurements.",
        "• Observe the phenomenon of wave function collapse."
    ]
    return bullets

def page_1_bullets():
    bullets = [
        "• Superposition is a fundamental principle of quantum mechanics.",
        "• A quantum system can exist in multiple states at the same time.",
        "• A qubit can be in a combination of the |0⟩ and |1⟩ states.",
        "• This is expressed as ψ = α|0⟩ + β|1⟩, where α and β are probability amplitudes.",
        "• Upon measurement, the state collapses to either |0⟩ or |1⟩.",
        "• Examples of superposition for 1, 2, and 3-qubit systems are shown below:"
    ]
    return bullets

def page_2_bullets():
    bullets = [
        "• In this stage, we’ll create and run a quantum circuit.",
        "• Superposition is achieved by applying Hadamard gates to individual qubits.",
        "• This should (in theory) give each state an equal chance of being measured.",
        "• However, due to noise or hardware imperfections, results may vary.",
        "• Let’s first take a look at the quantum circuit for a 3-qubit superposition..."
    ]
    return bullets

def page_3_1_bullets():
    bullets = [
        "• You've now seen what a quantum circuit looks like.",
        "• Now, we'll run and measure it — forcing the quantum system to select a single outcome.",
        "• In quantum computing, it's common to run the same circuit multiple times to estimate the probability distribution of all possible states.",
        "• These repetitions are called \"shots.\"",
        "• Ideally, each state should be equally likely — assuming perfect superposition and no noise.",
        "• In practice, we may observe deviations due to noise, decoherence, or gate imperfections."
    ]
    return bullets

def page_3_2_bullets(max_state, max_count):
    bullets = [
            f"• Most frequent state: {max_state} with count: {max_count}.",
            f"• Next, we will look at wave function collapse, and see what happens when a measurement is made!"
        ]

def page_4_1_bullets():
    bullets = [
        "• Before a quantum system is measured, all possible states exist with certain probabilities.",
        "• When a measurement occurs, the system is forced to 'choose' one of those possible outcomes.",
        "    • The higher the probability of a state, the more likely it is to be selected.",
        "• Once a choice is made, the probabilities collapse.",
        "    • The selected state now has a probability of 1.",
        "    • All other states drop to a probability of 0.",
        "• This phenomenon is known as 'Wave Function Collapse'.",
        "• It represents the transition from the quantum world to the classical world — where we observe only one outcome."
    ]
    return bullets

def page_4_2_bullets(selected):
    bullets = [
        f"• In our case, state {selected} was chosen"
    ]
    return bullets

def page_5_bullets():
    bullets = [
        "• You’ve learned that quantum systems can exist in superposition — being in multiple states at once.",
        "• You’ve seen how circuits can be used to create and manipulate quantum states.",
        "• You’ve explored how measurement causes the wave function to collapse, forcing the system to choose a specific state.",
        "• You’ve understood that real-world quantum results may diverge from theoretical predictions due to noise and imperfections.",
        "• You’ve observed how probability distributions emerge through repeated measurements, or 'shots'.",
        "• Thank you for playing Schrödinger’s Dice Game — we hope you had fun while learning!",
        "• You may now close the game window whenever you're ready."
    ]
    return bullets