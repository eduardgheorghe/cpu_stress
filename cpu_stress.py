import math
import time
import multiprocessing

def generate_cpu_load(duration):
    print(f"Creating CPU load for {duration} seconds...")
    processes = []

    # Start a separate process for each CPU core
    for _ in range(multiprocessing.cpu_count()):
        process = multiprocessing.Process(target=cpu_worker)
        process.start()
        processes.append(process)

    # Wait for the specified duration
    time.sleep(duration)

    # Terminate all CPU load generation processes
    for process in processes:
        process.terminate()

    print("CPU load generation complete.")

def cpu_worker():
    # Perform CPU-bound computations
    while True:
        # Perform some CPU-bound computations
        math.factorial(1000)

# Main script
if __name__ == "__main__":
    duration = int(input("Enter the duration (in seconds) for CPU load generation: "))
    generate_cpu_load(duration)

