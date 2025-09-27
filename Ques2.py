def maximizeSumOfSquares(K, M, lists):
    dp = {0}  # (sum=0)

    for lst in lists:
        new_dp = set()
        for val in lst:
            val_sq_mod = (val * val) % M
            for prev_sum in dp:
                new_sum = (prev_sum + val_sq_mod) % M
                new_dp.add(new_sum)
        dp = new_dp  

    return max(dp)

K = 3
M = 1000
lists = [
    [2, 4],
    [3, 6, 7],
    [5, 7, 8, 9, 11]
]
print(maximizeSumOfSquares(K, M, lists)) 
