'''
작성일:2023년10월4일
작성자:컴퓨터공학부 202095108 한송림
설명:더하기 암산 문제 만들기 
    2개의 수로 더하기 결과를 맞추는 게임.
    2개의 수는 1-100사이 랜덤으로 출제 됨
    사용자가 0을 입력하면 프로그램은 종료
    즉 ,사용자가 0을 입력하기 전까지는 무한 반복하여 문재 풀기
    정답을 맟추면 "참 잘했어요!"
    틈리면 정답을 알려주고,"정답은 00입니다.틈렸습니다." 출력
    
    문제 분석:랜뎀수 생성 => import random
                            random.randint(1,100)
    
    알고리즘:
'''

import random as r
num1 = r.randint(1, 100)
num2 = r.randint(1, 100)
z = num1 + num2
answer = 0

while True:
    num1 = r.randint(1, 100)
    num2 = r.randint(1, 100)
    z = num1 + num2
    answer = int(input(f"{num1}+{num2}="))
    if answer == 0:
        break

    if answer == z:
        print('잠 잘했어요!!')
    else:
        print('정답은', z, '입니다.틉렸습니다.')

    print("프로그램 종료!")
