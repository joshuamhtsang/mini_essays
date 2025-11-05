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
    print("Welcome to Chapter 02 Physical Layer Chains!")

    # Step 1: Define constellation
    NUM_BITS_PER_SYMBOL = 2 # QPSK
    constellation = sionna.phy.mapping.Constellation("qam", NUM_BITS_PER_SYMBOL)
    
    print(matplotlib.get_backend())
    print(type(constellation))
    constellation.show()
    plt.show()

    print("constellation = ", constellation.points)

    # Step 2: Define the mapper and demapper
    mapper = sionna.phy.mapping.Mapper(constellation=constellation)

    # The demapper uses the same constellation object as the mapper
    demapper = sionna.phy.mapping.Demapper("app", constellation=constellation, hard_out=False)

    # Step 3: Define a binary source
    binary_source = sionna.phy.mapping.BinarySource()

    # Chain 1: Proceed with a basic chain
    BATCH_SIZE = 16 # How many examples are processed by Sionna in parallel

    bits = binary_source([BATCH_SIZE, 256]) # Blocklength
    print("Shape of bits: ", bits.shape)
    print(bits)

    symbols = mapper(bits)
    print(symbols)

    no = sionna.phy.utils.ebnodb2no(ebno_db=10.0, num_bits_per_symbol=NUM_BITS_PER_SYMBOL, coderate=1.0)

    decoded_bits = demapper(symbols, no)
    print(decoded_bits)

    # Plot post-channel symbols
    plt.figure(figsize=(8,8))
    plt.axes().set_aspect(1)
    plt.grid(True)
    plt.title('Channel output')
    plt.xlabel('Real Part')
    plt.ylabel('Imaginary Part')
    plt.scatter(tf.math.real(symbols), tf.math.imag(symbols))
    plt.tight_layout()
    plt.show()

