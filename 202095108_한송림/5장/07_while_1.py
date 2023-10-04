'''
작성일:2023년10월4일
작성자:컴퓨터공학부 202095108 한송림
설명:조건에 따라 반복하는 while문
'''
# while 조건식 : => : 반드시 사용.
#   들여쓰기로 반복하면서 할일 작성.

under_construction = True

# True일 동안 계속 반복
while under_construction:
    response = input("공사가 완료 되었습니까?")
    if response == "에":
        under_construction = False

print("루프 탈츨!!!")
