import sionna

import os

if __name__ == "__main__":
    if os.getenv("CUDA_VISIBLE_DEVICES") is None:
        gpu_num = 0 # Use "" to use the CPU
        os.environ["CUDA_VISIBLE_DEVICES"] = f"{gpu_num}"
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

    print(gpu_num)
