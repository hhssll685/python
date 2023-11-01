'''
작성일:2023년 11월 1일
적성자:컴퓨터공학부 202096108 한송림
설명:LAB 8-1 편의점 재고 관리 프로그램
'''

items = {"커피음료":7,"펜":3,"종이컵":2,"우유":1,"콜라":4,"책":5}

print('제품 목록:' ,end='')
for key in items.keys() :
    print(key,end=', ')
print()

name = input("물건의 이름을 입력하시오:")
print('재고:',items[name])