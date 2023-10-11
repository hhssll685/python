"""
작성일:2023년10월11일
작성자:컴퓨터공학부 202095108 한송림
설명:함수의 디폴트 인자
"""


def order(num, pickel, onion):
    print("햄버거{}개-피클{},양파{}".format(num, pickel, onion))


def order2(num, pickel="기본", onion="기본"):
    print("햄버거{}개-피클{},양파{}".format(num, pickel, onion))


order2(1)
order2(1, pickel="뱀", onion="기본")
