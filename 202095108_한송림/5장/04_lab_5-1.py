'''
작성일:2023년9월27일
작성자:컴퓨터공학부 202095108 한송림
설명:터를 그래픽으로 여러 개의 원을 그려보자
'''
import turtle as t
# 원 하나 그리기
# t.circle(100)
for count in range(5):
    t.circle(100)
    t.left(360/5)

t.mainloop()  # 종료
# t.done()#종료
