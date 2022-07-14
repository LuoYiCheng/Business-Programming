# 定義一個判斷是否為質數的函數
def is_prime(x):
    '''determine whether the number is prime'''
    ans = True
    if x == 1:
        ans = False
    else:
        for i in range(2, int(x/2)+1):
            if x % i == 0:
                ans = False
                break
    return ans

# Input variables
n_k = [int(i) for i in input().split(',')]
n = n_k[0]
k = n_k[1]

# 演算法
result = []
for i in range(1, n+1):
    if (is_prime(i) == True) or (i % k == 0):
        result.append(i)
    else:
        continue
print(','.join(str(i) for i in result))