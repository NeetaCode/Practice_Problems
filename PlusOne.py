def PlusOne(digits):
    num = ""
    
    for i in range(len(digits)):
        num += str(digits[i])
    
    
    
    num = int(num) + 1
    
    res = [int(digit) for digit in str(num)]
    
    #print(num)
    return num
    
print(PlusOne([1,2,3]))
