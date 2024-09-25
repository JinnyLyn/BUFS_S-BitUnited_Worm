#만든 비밀번호가 안전한지에 따라서 등급을 메기는 시스템

import re

def  chk (a, b, c, d) :
  return a in d or b in d or c in d

#비번 안전도 수준
score=0

#이름 설정
name = input("이름을 입력하세요: ")


 #생일 설정
birth = input("생일을 4자리로 입력하세요: ")
while len(birth) != 4 or not birth.isdigit(): #4자리가 아니면 다시
    print("잘못 입력하셨습니다. 생일을 4자리 숫자로 다시 입력해주세요.")
    birth = input("생일을 4자리로 입력하세요: ")


#전번 설정
phone = input("전화번호 뒷자리 8자리를 입력하세요: ") 
while len(phone) != 8 or not phone.isdigit(): #8자리가 아니면 다시
    print("잘못 입력하셨습니다. 전화번호를 8자리 숫자로 다시 입력해주세요.")
    phone = input("전화번호 뒷자리 8자리를 입력하세요: ")


#사용할 비번 설정
password = input("비밀번호를 설정하세요: ") 
test = input("설정한 비밀번호를 한 번 더 입력하세요: ") #맞는지 확인

if test != password : #같지 않으면 다시
    print("비밀번호가 같지 않습니다.")
    quit()

#개인정보가 비번에 있는지
while chk (name, birth, phone, password):
    print("비밀번호에 이름, 생일, 전화번호가 포함되어 있습니다. 다시 설정해주세요.")
    quit()

#길이 평가
if len(password) >= 8: 
        if len(password) >= 12:
            score += 20
        else:
            score += 10
else:
    print("비밀번호는 최소 8자 이상이어야 합니다.")
    quit()
    
#대문자 포함 여부 평가
uppercase = len(re.findall(r'[A-Z]', password))
if uppercase >= 1:
    if uppercase >= 3:
            score += 20
    elif uppercase >= 2:
            score += 10
else:
    input("비밀번호에 최소 1개의 대문자가 필요합니다.")
    quit()
    
#숫자 포함 여부 평가
if re.search(r'\d', password):
        score += 20
else:
    input("비밀번호에 최소 1개의 숫자가 필요합니다.")
    quit()    

#특수문자 포함 여부 평가
special_char_count = len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password))
if special_char_count >= 1:
    if special_char_count >= 2:
            score += 20
    else:
            score += 10
else:
    print("비밀번호에 최소 1개의 특수 문자가 필요합니다.")
    quit() 

#비번 수준 평가
if score < 40:
    print(f"비밀번호 강도: {score}점 (다시 설정 필요)")
elif 40 <= score < 60:
    print(f"비밀번호 강도: {score}점 (평균)")
elif 60 <= score < 80:
    print(f"비밀번호 강도: {score}점 (안전)")
else:
    print(f"비밀번호 강도: {score}점 (매우 안전)")

