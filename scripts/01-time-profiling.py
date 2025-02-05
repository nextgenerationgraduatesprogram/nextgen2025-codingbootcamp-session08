import time
import random
import multiprocessing as mp

# lets define some task to perform
def job_with_fixed_execution_time(x: int):
    """
    execution time is a fixed 1.0s
    """
    time.sleep(1)
    return x ** 2


if __name__ == "__main__":
    # define a simple set of inputs to the job
    inputs = [1,2,3,4,5]
    outputs = []

    # perform a job
    for val in inputs:
        output = job_with_fixed_execution_time(val)
        outputs.append(output)

    print(f"{inputs} -> job -> {outputs}")
