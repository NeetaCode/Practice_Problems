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
