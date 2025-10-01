def getHighLoadTimestamps(load):
    n = len(load)
    avg = sum(load) / n
    threshold = 2 * avg
    
    result = [i for i, val in enumerate(load) if val > threshold]
    return result


# ----------- Testing with provided examples ------------

# Example 1
load1 = [1, 2, 9]
print(getHighLoadTimestamps(load1))  # Expected [2]

# Example 2
load2 = [1, 1, 7, 7, 1]
print(getHighLoadTimestamps(load2))  # Expected [2, 3]

# Example 3
load3 = [3, 3, 3, 3]
print(getHighLoadTimestamps(load3))  # Expected []
