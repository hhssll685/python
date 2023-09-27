'''
작성일:2023년9월27일
작성자:컴퓨터공학부 202095108 한송림
설명:터를 그래픽으로 N각형 도형을 그려보자
사용자로부터 그리고싶은 도형의 변의 수를 입력 받아
도형을 그린다
'''
import turtle as t
t.shape("turtle")
t.penup()
t.goto(-50, -50)
t.pendown()  # 이동을 마치면 펜을 내려 놓는다.
# 원하는 도형을 입역 받는다. => 변수에 저장.
for i in range(5):
    num = int(t.textinput("도형그리기", "몇각형의 도형을 그릴까요?"))

    for i in range(num):
        t.forward(100)
        t.left(360/num)

t.done()
