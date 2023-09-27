'''
작성일:2023년9월27일
작성자:컴퓨터공학부 202095108 한송림
설명:range()한수
'''
for i in range(3):
    print(i, end='.')
    print("안녕하세요.")
    print("한송림입니다.")

# range(시작값,숫자 앞까지,증가값(감소값))
# C언어 -> for(츠기값;조건식;중감식)
for i in range(1, 6):
    print(i, end=' ')

print()  # 변줄 출력


# 10~1까지 출력
for i in range(10, 0, -1):
    print(i, end=' ')
