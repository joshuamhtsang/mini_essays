import os
import sionna

def main():
    print("Hello from 01-installation!")


if __name__ == "__main__":
    if os.getenv("CUDA_VISIBLE_DEVICES") is None:
        gpu_num = 0 # Use "" to use the CPU
        os.environ["CUDA_VISIBLE_DEVICES"] = f"{gpu_num}"
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

    print("Number of gpus detected:", gpu_num)

    main()
