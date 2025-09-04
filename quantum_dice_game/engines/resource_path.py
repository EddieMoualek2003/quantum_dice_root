## This module is a bit strange in the sense that all it does is return the relative resources folder path for the files needed.

import os

def superpos_equations():
    base_dir = os.path.dirname(__file__)
    resource_dir = os.path.join(base_dir, "..", "resource_folder_gen")
    resource_dir = os.path.abspath(resource_dir)

    os.makedirs(resource_dir, exist_ok=True)

    out_path = os.path.join(resource_dir, "superposition_all.png")
    return out_path

def quantum_circuit_image():
    base_dir = os.path.dirname(__file__)
    resource_dir = os.path.join(base_dir, "..", "resource_folder_gen")
    resource_dir = os.path.abspath(resource_dir)

    os.makedirs(resource_dir, exist_ok=True)

    # Return the full path as a string
    out_path = os.path.join(resource_dir, "circuit.png")
    return out_path

def quantum_circuit_pkl():
    base_dir = os.path.dirname(__file__)
    resource_dir = os.path.join(base_dir, "..", "resource_folder_gen")
    resource_dir = os.path.abspath(resource_dir)

    os.makedirs(resource_dir, exist_ok=True)

    # Return the full path as a string
    out_path = os.path.join(resource_dir, "created_circuit.pkl")
    return out_path

def quantum_circuit_counts_pkl():
    base_dir = os.path.dirname(__file__)
    resource_dir = os.path.join(base_dir, "..", "resource_folder_gen")
    resource_dir = os.path.abspath(resource_dir)

    os.makedirs(resource_dir, exist_ok=True)

    # Return the full path as a string
    out_path = os.path.join(resource_dir, "counts.pkl")
    return out_path

def wf_collapse_gif_path():
    base_dir = os.path.dirname(__file__)
    resource_dir = os.path.join(base_dir, "..", "resource_folder_gen")
    resource_dir = os.path.abspath(resource_dir)

    os.makedirs(resource_dir, exist_ok=True)

    # Return the full path as a string
    out_path = os.path.join(resource_dir, "schrodinger_dice_wavefunction_collapse.gif")
    return out_path

def iam_response_path():
    base_dir = os.path.dirname(__file__)
    resource_dir = os.path.join(base_dir, "..", "resource_folder_gen")
    resource_dir = os.path.abspath(resource_dir)

    os.makedirs(resource_dir, exist_ok=True)

    # Return the full path as a string
    out_path = os.path.join(resource_dir, "iam_response.pkl")
    return out_path