######################## MY THOUGHT VERSION #######################################################

def fill_dict(arr, k):

    res = {}
    count = 0
    
    for i in range(len(arr)):
        if arr[i] not in res:
            count = 1
            res[arr[i]] = count
            
        else:
            count += 1
            res[arr[i]] = count
            
    count = 0
    
    r=max(res.values())
    lr = { res[r]:r }
    print(lr)
    
    return lr
    
fill_dict([1,1,1,2,2,3],2)



######################## EXPECTED VERSION #######################################################

import heapq

def top_k_frequencies_no_dict(arr, k):
    pq = []  # min-heap storing (frequency, element) tuples

    for num in arr:
        found = False
        # Search heap to see if num is already present
        for i in range(len(pq)):
            if pq[i][1] == num:
                freq_old, _ = pq[i]
                # Remove old tuple
                pq[i] = pq[-1]
                pq.pop()
                heapq.heapify(pq)
                # Push updated frequency
                heapq.heappush(pq, (freq_old + 1, num))
                found = True
                break

        if not found:
            heapq.heappush(pq, (1, num))  # first occurrence

        # Keep only top k elements
        if len(pq) > k:
            heapq.heappop(pq)

    # Extract elements from heap
    result = []
    while pq:
        freq_val, key = heapq.heappop(pq)
        result.append((key, freq_val))

    result.reverse()  # largest frequency first
    for key, freq_val in result:
        print(key, freq_val)

    return result

# Example usage
top_k_frequencies_no_dict([1, 1, 1, 2, 2, 3], 2)

