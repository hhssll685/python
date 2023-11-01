'''
작성일:2023년 11월 1일
적성자:컴퓨터공학부 202096108 한송림
설명:LAB 7-5 함수는 튜플을 돌려줄 수 있다.

    반지름을 입력받아 원의 넓이와 돌레를 계산하시오.
    넓이와 둘레를 계산하는 함수를 작성하시오.
    함수는 넚이와 둘레를 함께 둘려줍니다.(return)

    [함수]
        3.반지름을 입력 받는다.
    [메인]
        1.반지름을 입력 받는다.
        2.함수 호출 -> 반지름을 가지고 호출한다.

    [메인]
        1.반지름을 입력 받는다.
        2.함수 호출 -> 반지름을 가지고 호출한다.
        6.돌려받은 넓이와 둘레를 튜플로 저장한다.
        7.출력한다.
'''
import math
def calCircle(r):
    area=math.pi*r*r
    circum = 2 * math.pi * r
    return area,circum

radius = float(input("원의 반지름을 입력하시오."))
(area,circum) = calCircle(radius)
print(f"번지름이{radius}인 원의 넓이는{area:.2f}이고,원의 둘레는{circum:.2f}이다.")

circle=calCircle(radius)
print(f"반지름이{radius}인 원의 넓이는 {circle[0]:.2f}이고,원의 둘레는{circle[1]:.2f}이다.")