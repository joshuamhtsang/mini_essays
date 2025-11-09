# Set GPU env vars
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sionna.phy
import tensorflow as tf


if os.getenv("CUDA_VISIBLE_DEVICES") is None:
    gpu_num = 0 # Use "" to use the CPU
    os.environ["CUDA_VISIBLE_DEVICES"] = f"{gpu_num}"

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


if __name__ == "__main__":
    print("Welcome to Chapter 03 Sionna Blocks and FEC!")

    