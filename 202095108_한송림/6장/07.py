"""
작성일:2023년10월11일
작성자:컴퓨터공학부 202095108 한송림
설명:

리스트에 10개의 값을 랜덤으로 생성하고,
max 또는 min을 입력 받아 최대,최소값을 찾아 들려주는 함수.

(함수)
    5)두 값을 전달받아 매개 변수에 저장.
    6)최대값,최소값을 찾는다. max(),min()
    7)값을 돕려준다.
(메인)
1.무한반복
    1)런댐으로 10-99까지 10개의 수를 리스트로 생성
    2)생성된 리스트를 출력
    3)사용자로부터 최대값은 알고 싶은지 최소값을 알고 싶은지 묻는다.
    사용자가 입력할 값은 max 또는 min
    4)입력받은 max또는 min과 생성된 리스트를 가지고 함수 호출
    5)돌려 받은 최대값 또는 최소값을 출력한다.
"""
import random as r


def getMinMax(list, input):
    if input == "max":
        max_num = list[0]
        for i in list:
            if i > max_num:
                max_num = i
        return max_num
    elif input == "min":
        min_num = list[0]
        for i in list:
            if i < min_num:
                min_num = i
        return min_num
    else:
        print("illegal input")
    print()


while True:
    mList = [r.randint(1, 100) for i in range(10)]
    while True:
        print(mList)
        mInput = input("max 또는 min을 입력하여 목록을 정렬합니다:")
        print(getMinMax(mList, mInput))
