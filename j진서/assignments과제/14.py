# 과제 14

def 약수구하기(n):
    divisors = []
    for i in range(1, n+1):
        if (n % i == 0):
            divisors.append(i)
    return divisors

result = 약수구하기(12)
print(result)