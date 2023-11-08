'''
작성일:2023년 11월 8일
적성자:컴퓨터공학부 202095108 한송림
설명:집합의 연산
'''
#비교 연산자
num1 = {1,2,3}
num2 = {1,2,3}
print("num1 == num2 ?",num1 == num2)

#6개의 숫자로 집합 생성
num_set={1,4,6,3,7,4}
print("num_set: ",num_set)
print("num_set 길이 : ",len(num_set))
print("num_set 중 가장 큰 값 :",max(num_set))
print("num_set 중 가장 작은 값 :",min(num_set))
print("num_set 합계 : ",sum(num_set))


num1 = {1,2,3}
num2 = {3,4,5}

#합집합
print('num1 | num2 :',num1 | num2)#합집한 연산자
print('(num2) :',num1.union(num2))#합집한 메소드 union()

