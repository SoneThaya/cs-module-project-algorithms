'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache={0:1, 1:1, 2:2}):
    # Your code here
   
    # if n < 0:
    #     return 0
    # if n == 0:
    #     return 1
    # elif n in cache:
    #     return cache[n]
    # else:
        
    #     cache[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    #     return cache[n]
    if n in cache:
        return cache[n]
    else:
        cache[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
        return cache[n]
    


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
