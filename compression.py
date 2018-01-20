import numpy as np

# Takes a 2D array of history of automata (bitmap)
def runlength(bmp):
    lin_data = bmp.flatten()
    compressed = []

    run_total = 0
    for i in range(len(lin_data)-1):
        if lin_data[i] == lin_data[i+1]:
            run_total += 1
        else:
            compressed.extend([run_total, lin_data[i]])
            run_total = 0

    return np.array(compressed)
