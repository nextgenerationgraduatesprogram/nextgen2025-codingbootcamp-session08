import pandas as pd
from memory_profiler import profile


@profile
def memory_intensive_function():
    # say this doesnt fit into memory
    df = pd.read_csv("../data/huge_file.csv") # e.g. 100TiB of memory?!
    df["transaction_value"].sum()


if __name__ == "__main__":
        _ = memory_intensive_function()
