#만든 비밀번호가 안전한지에 따라서 등급을 메기는 시스템

name = input("이름을 입력하세요: ") #이름 설정

birth = input("생일을 4자리로 입력하세요: ") #생일 설정
while len(birth) != 4 or not birth.isdigit(): #4자리가 아니면 다시
    print("잘못 입력하셨습니다. 생일을 4자리 숫자로 다시 입력해주세요.")
    birth = input("생일을 4자리로 입력하세요: ")

phone = input("전화번호 뒷자리 8자리를 입력하세요: ") #전번 설정
while len(phone) != 8 or not phone.isdigit(): #8자리가 아니면 다시
    print("잘못 입력하셨습니다. 전화번호를 8자리 숫자로 다시 입력해주세요.")
    phone = input("전화번호 뒷자리 8자리를 입력하세요: ")

password = input("비밀번호를 설정하세요: ") #사용할 비번 설정
test = input("설정한 비밀번호를 한 번 더 입력하세요: ") #맞는지 확인

if test != password : #같지 않으면 다시
    print("비밀번호가 같지 않습니다.")
    quit()
    


