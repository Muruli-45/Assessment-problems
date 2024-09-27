n = int(input())
if n == 0:
    print(-1)
else:
    arr = list(map(int, input().split()))
    num = int(input())
    prime_factors = []
    original_num = num
    for i in range(2, int(num**0.5) + 1):
        while num % i == 0:
            prime_factors.append(i)
            num //= i
    if num > 1:
        prime_factors.append(num)
    unique_factors = set(prime_factors)
    sum_result = 0
    found_valid_index = False
    for factor in unique_factors:
        index = factor - 1  
        if 0 <= index < n: 
            sum_result += arr[index]
            found_valid_index = True
    if found_valid_index:
        print(sum_result)
    else:
        print(0)