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
    plt.close()

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
    print("bits = \n", bits)

    symbols = mapper(bits)
    print(symbols)

    # Define channel
    ebno_db = -1.0
    no = sionna.phy.utils.ebnodb2no(ebno_db=ebno_db, num_bits_per_symbol=NUM_BITS_PER_SYMBOL, coderate=1.0)
    print("ebno_db = ", ebno_db, ", no = ", no)

    awgn_channel = sionna.phy.channel.AWGN()
    noisy_symbols = awgn_channel(symbols, no)

    llr = demapper(noisy_symbols, no)
    print(llr)

    # Plot noisy symbols
    plt.figure(figsize=(8,8))
    plt.axes().set_aspect(1)
    plt.grid(True)
    plt.title(f'Noisy Symbols at ebno = {ebno_db} dB')
    plt.xlabel('Real Part')
    plt.ylabel('Imaginary Part')
    plt.scatter(tf.math.real(noisy_symbols), tf.math.imag(noisy_symbols))
    plt.tight_layout()
    plt.show()
    plt.clf()
    plt.close()

    # Loop through several values of ebno_db

    # Lists for BER vs ebno plot
    x_vals_ebno = []
    y_vals_ber = []

    for ebno_db in range(-10, 10, 2):
        no = sionna.phy.utils.ebnodb2no(ebno_db=ebno_db, num_bits_per_symbol=NUM_BITS_PER_SYMBOL, coderate=1.0)
        print("ebno_db = ", ebno_db, ", no = ", no)
        noisy_symbols = awgn_channel(symbols, no)
        llr = demapper(noisy_symbols, no)

        # Compute bit error rate (BER)
        decoded_bits = sionna.phy.utils.hard_decisions(llr)
        #print("decoded_bits = \n", decoded_bits)
        ber = sionna.phy.utils.compute_ber(bits, decoded_bits)
        print("ber = ", ber)
        x_vals_ebno.append(ebno_db)
        y_vals_ber.append(ber.numpy())

        # Plot noisy symbols
        plt.figure(figsize=(8,8))
        plt.axes().set_aspect(1)
        plt.grid(True)
        plt.title(f'Noisy Symbols at ebno = {ebno_db} dB')
        plt.xlabel('Real Part')
        plt.ylabel('Imaginary Part')
        plt.scatter(tf.math.real(noisy_symbols), tf.math.imag(noisy_symbols))
        plt.tight_layout()
        #plt.savefig(f'noisy_symbols_{ebno_db}.png')
        plt.clf()
        plt.close()
    
    print(x_vals_ebno, y_vals_ber)

    plt.grid(True)
    plt.title(f'BER vs ebno plot for QAM at {NUM_BITS_PER_SYMBOL} bits per symbol')
    plt.xlabel('ebno (dB)')
    plt.ylabel('BER')
    plt.scatter(x_vals_ebno, y_vals_ber, label="Uncoded")
    plt.yscale('log')
    plt.legend(loc="upper right")
    plt.show()
    plt.clf()
    plt.close()
