'''
작성일:2023년9월20일
작성자:컴퓨터공학부 202095108 한송림
설명:선택문 if-else
    정수를 입력받아 짝수인지 홀수인지 판다.
    짝수,홀수는 양수임 경우에만 판단한다.
    
    짝수 = 2로 나눈 나머지가 0이다. %,==
    홀수 = 2로 나눈 나머지가 1이다.(0이 아니다.)
'''
# 1.
num = int(input("정수 입력:"))
# 2.
if num > 0:
    # 2-1
    if num % 2 == 0:
        print(f"{num}은(는) 짝수입니다.")
    else:
        print(f"{num}은(는) 홀수입니다.")
else:
    print(f"{num}은(는) 음수입니다.")
# 3.
