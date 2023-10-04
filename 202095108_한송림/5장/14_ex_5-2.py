'''
작성일:2023년10월4일
작성자:컴퓨터공학부 202095108 한송림
설명:두 수를 입력 빋아 
    1.두 수 사이의 합계 출력하기
    2.두 수 사이의 짝수의 합계 출력하기
    
    심화문제5.2,141쪽
    for 또는 while 중 원하는 것 사용.
    
    오늘의 마지막 문제 
    주석 없으면 0점
'''
while True:

    num1 = int(input("숫자 입력:"))
    num2 = int(input("숫자 입력:"))
    result0 = 0
    result1 = 9

    for i in range(num1, num2+1):
        result0 += i
        if (i % 2 == 0):
            result1 += i

    print(f"{num1}에서 {num2}의 합은 {result0}입니다.")
    print(f"{num1}에서 {num2}의 짝수의 합은 {result1}입니다.")
    stop = input("계속하려면 Enter 키를 입력하십시오.")
    if stop:
        break
