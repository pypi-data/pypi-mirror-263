"""
Training functions
"""

import torch


def get_device(use_mps=True):
    """Return the available GPU/CPU device"""

    if torch.cuda.is_available():
        device = torch.device("cuda")
        message = f"Using CUDA GPU {torch.cuda.get_device_name(0)} :)"
    elif use_mps and torch.backends.mps.is_available():
        device = torch.device("mps")
        message = "Using MPS GPU :)"
    else:
        device = torch.device("cpu")
        message = "No GPU found, using CPU instead"

    return device, message
