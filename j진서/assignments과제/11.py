# 과제 11

# Exit Codes
# -1     : input error
# 0      : no err
# others : input err

score = 0

try:
    score = int(input('점수 입력: '))
    if not (0 <= score <= 100) or score < 0:
        print('점수입력 똑바로하세요')
        exit(-1)
except ValueError:
    print("점수입력 똑바로하세요")

if score >= 90:
    print(f'{score}점은 A학점입니다.')
elif score >= 80:
    print(f'{score}점은 B학점입니다.')
elif score >= 70:
    print(f'{score}점은 C학점입니다.')
elif score >= 60:
    print(f'{score}점은 D학점입니다.')
else:
    print(f'{score}점은 F학점입니다.')

exit(0)
