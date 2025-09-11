def getHighLoadTimestamps(load):
    n = len(load)
    avg = sum(load) / n
    threshold = 2 * avg
    result = [i for i, val in enumerate(load) if val > threshold]
    return result


if __name__ == "__main__":
    # Read input
    n = int(input().strip())
    load = [int(input().strip()) for _ in range(n)]
    
    # Get result
    result = getHighLoadTimestamps(load)
    
    # Print output
    print(result)
