import time
import timeit
import random
import numpy as np
import multiprocessing as mp


def matrix_multiply(A, B):
    # Create the result matrix with zeros
    output = np.zeros((A.shape[0], B.shape[1]))
    # Perform matrix multiplication
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            output[i][j] = sum(A[i][k] * B[k][j] for k in range(A.shape[1]))
    return output


# lets define some task to perform
def job_with_fixed_execution_time(x: int):
    """
    execution time is a fixed 1.0s
    """
    sz = 100
    A = np.random.randn(sz,sz)
    B = np.random.randn(sz,sz)
    output = matrix_multiply(A, B)
    # time.sleep(1)
    return x ** 2


def job_with_fixed_execution_time_and_two_args(x: int, y: int):
    """
    execution time is a fixed 1.0s
    """
    sz = 100
    A = np.random.randn(sz,sz)
    B = np.random.randn(sz,sz)
    output = matrix_multiply(A, B)
    return x ** 2 + y ** 2


def job_with_variable_execution_time(x: int):
    """
    execution time is random
    """
    sz = random.randint(50, 150)
    A = np.random.randn(sz,sz)
    B = np.random.randn(sz,sz)
    output = matrix_multiply(A, B)
    return x ** 2


def job_with_dependent_execution_time(t: int):
    """
    execution time depends on the input
    """
    t += 1
    sz = random.randint(50 * t)
    A = np.random.randn(sz,sz)
    B = np.random.randn(sz,sz)
    output = matrix_multiply(A, B)
    return t ** 2



if __name__ == "__main__":
    # benchmark job
    N = 1
    execution_time = timeit.timeit(lambda: job_with_fixed_execution_time(0), number=N)
    print(f"Execution Time: {execution_time/N:.3f} seconds")


    # define a simple set of inputs to the job
    inputs = range(1)

    # number of processes to distribute across
    n_processes = 1

    # spawn the processes
    with mp.Pool(processes=n_processes) as pool:
        # map the inputs to the job across processes
        """
        synchronous mapping applies a function to an iterable and blocks until all
        results are available.

        worker1: 
        worker2: 
        worker3: 
        worker4: 
        worker5: 
        worker6: 

        """
        t = time.perf_counter_ns()
        outputs = pool.map(
            job_with_fixed_execution_time, 
            inputs # has to be an iterable which returns a single item
        )
        t = time.perf_counter_ns() - t
        print(f"{inputs} -> job -> {outputs}")
        print(f"`map` execution took {t/1e9:.3f} s\n")












        # # # map asychronously
        # """
        # asynchronous mapping applies a function to an iterable and returns immediately 
        # without blocking, allowing code to continue execution without wait for computation
        # """
        # t = time.perf_counter_ns()
        # outputs = pool.map_async(
        #     job_with_fixed_execution_time,
        #     inputs            
        # )
        # outputs = outputs.get(timeout=10) # wait for jobs to be done
        # t = time.perf_counter_ns() - t
        # print(f"{inputs} -> job -> {outputs}")
        # print(f"`map_async` execution took {t/1e9:.3f} s\n")


        # # iteratively map asychronously
        # """
        # iterative mapping with unordered results as an asynchronous mapping method where the results
        # are yielded as the job finished but the order may not correspond to the input order
        # """
        # t = time.perf_counter_ns()
        # outputs = pool.imap_unordered(
        #     job_with_dependent_execution_time,
        #     inputs # [0.1, 0.2, 0.3, 0.45, 0.1]            
        # )
        # outputs = [output for output in outputs]
        # t = time.perf_counter_ns() - t
        # print(f"{inputs} -> job -> {outputs}")
        # print(f"`imap_unordered` execution took {t/1e9:.3f} s\n")


        # # map with multiple inputs
        # """
        # star mapping refers to mapping with non-keyword arguments to the function enabling multiple inputs
        # to be provided (given the correct order)
        # """
        # t = time.perf_counter_ns()
        # outputs = pool.starmap(
        #     job_with_fixed_execution_time_and_two_args, 
        #     zip(inputs, inputs) # iterable which may return multiple items
        # )
        # t = time.perf_counter_ns() - t
        # print(f"{inputs} -> job -> {outputs}")
        # print(f"`starmap` execution took {t/1e9:.3f} s\n")


        # # map asyncronously with multiple inputs
        # """
        # asynchronous star mapping refers to mapping with non-keyword arguments to the function enabling multiple 
        # inputs to be provided and code to continue running without blocking.
        # """
        # t = time.perf_counter_ns()
        # outputs = pool.starmap_async(
        #     job_with_fixed_execution_time_and_two_args,
        #     zip(inputs, inputs)
        # )
        # outputs = outputs.get(timeout=30) # have to wait for it to be done explicitly
        # t = time.perf_counter_ns() - t
        # print(f"{inputs} -> job -> {outputs}")
        # print(f"`starmap_async` execution took {t/1e9:.3f} s\n")

