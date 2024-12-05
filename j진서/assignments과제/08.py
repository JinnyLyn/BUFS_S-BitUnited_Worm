# 과제 08

# 1.) 4x^2 + 6x - 3
4*x**2 + 6*x - 3

# 2.) 근의공식
import math

dis = b**2 - 4*a*c
if dis < 0:
    print("근 없음")
    exit()

root1 = (-b + math.sqrt(dis)) / (2*a)
root2 = (-b - math.sqrt(dis)) / (2*a)
print(f'결과: {root1}, {root2}')
exit()