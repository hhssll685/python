'''
작성일:2023년9월20일
작성자:컴퓨터공학부 202095108 한송림
설명:선택문 if-else
    random 을 이용한 가위바위보 게임.
    
    random함수로 생성된 정수를 가지고 게임을 진행힙니다.
    0 => 가위
    1 => 바위
    2 => 보
    
'''

import random

print(":: 가위 바위 보 게임 시작 ::")

player1 = input("Player1의 이름:")
player2 = input("Player2의 이름:")

num1 = random.randrange(3)
num2 = random.randrange(3)

choices = ["가위", "바위", "보"]
choice1 = choices[num1]
choice2 = choices[num2]

print(f"{player1}, {choice1}로 합니다.")
print(f"{player2}, {choice2}로 합니다.")

if choice1 == choice2:
    print("무승부입니다.")
elif (choice1 == "가위" and choice2 == "보") or (choice1 == "바위" and choice2 == "가위") or (choice1 == "보" and choice2 == "바위"):
    print(f"{player1}이 미겼습니다.")
else:
    print(f"{player2}이 미겼습니다.")
