'''
작성일:2023년 10월 18일
적성자:컴퓨터공학부 202096108 한송림
설명:리스트의 객체 생성과 참조
'''

fruits1=['딸기','수박','바나나']

fruits2 = fruits1

print("fruits1 : ",fruits1)
print("fruits2 : ",fruits2)

fruits2[1]='망고'

print("fruits1 : ",fruits1)
print("fruits2 : ",fruits2)

print("fruits1의 id : " ,id(fruits1))
print("fruits2의 id : " ,id(fruits2))

'''
    리스트 내용 목제하기 list()함수
'''

fruits2=list(fruits1)
print("::내용 복제 후1::")
print("fruits1 : ", fruits1)
print("fruits2 : ", fruits2)

print("fruits1의 id : " ,id(fruits1))
print("fruits2의 id : " ,id(fruits2))

fruits3=fruits1[:]

print("::내용 복재 후2::")
print("fruits1 : ", fruits1)
print("fruits3 : ", fruits3)

print("fruits1의 id : " ,id(fruits1))
print("fruits3의 id : " ,id(fruits3))

fruits3[0] = '수박'
print("::fruits3의 0번지에 수박으로 내용 바꾼 후::")
print("fruits1 :",fruits1)
print("fruits3 :",fruits3)


'''
'''

print("과일 목록:",fruits1)
print("과일 리스트 중 2,3,4번 과일은?",fruits1[1:4])
print("과일 리스트 중 1-3번 과일은?",fruits1[0:3])
print("과일 리스트 중 1-3번 과일은?",fruits1[:3])
print("과일 리스트 중 3번 과일부터 마지막까지 과일은?",fruits1[2:])

print("과일 리스트 중 1,3,5번 과일은?",fruits1[::2])
print("과일을 거꾸로 출력",fruits1[::-1])