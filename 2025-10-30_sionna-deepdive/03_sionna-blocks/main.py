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

# First define a Sionna block class for an uncoded comms chain
class UncodedAWGN(sionna.phy.Block):
    def __init__(self, num_bits_per_symbol, block_length):
        self.num_bits_per_symbol = num_bits_per_symbol
        self.block_length = block_length
        self.constellation = sionna.phy.mapping.Constellation("qam", self.num_bits_per_symbol)
        self.mapper = sionna.phy.mapping.Mapper(constellation=self.constellation)
        self.demapper = sionna.phy.mapping.Demapper("app", constellation=self.constellation)
        self.binary_source = sionna.phy.mapping.BinarySource()
        self.awgn_channel = sionna.phy.channel.AWGN()

    def call(self, batch_size, ebno_db):
        # no channel coding used; we set coderate=1.0
        no = sionna.phy.utils.ebnodb2no(ebno_db, num_bits_per_symbol=self.num_bits_per_symbol, coderate=1.0)
    
        bits = self.binary_source([batch_size, self.block_length])
        x = self.mapper(bits)
        y = self.awgn_channel(x, no)
        llr = self.demapper(y,no)

        return bits, llr


if __name__ == "__main__":
    print("Welcome to Chapter 03 Sionna Blocks and FEC!")

    model_uncoded_awgn = UncodedAWGN(num_bits_per_symbol=2, block_length=256)

    