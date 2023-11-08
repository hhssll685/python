'''
작성일:2023년 11월 8일
적성자:컴퓨터공학부 202095108 한송림
설명:심화문제 8-3

1.학번,이름,전화번호의 3쌍의 요쇼를 가지는
  student_tuple라는 튜플이 존재한다.

2.이 튜플을 수정하여{학번 : [이름,전화번호]}의 쌍으로
  이루어진 딕셔너리를 출력하시오.

3.이 정보를 이용하여 학생의 학번을 입력 받아
  이름과 전화번호를 출력하는 학사정보 프로그램을 작성

4.student_tuple의 마지막 항목으로 학점을 추가한다.
  이 정보를 바탕으로 딕셔너를 만들어 출력하시오.

5.학생의 학점 평규을 출력하시오
'''
student_tuple = [('202095001','홍길동','010-1234-5678'),('202095002','홍은효','010-9876-5432'),('202095002','한림효','010-3579-1367')]

student_dict = {}
#1. 딕셔너리에 추가
for id_num,name,phone in student_tuple:
    student_dict[id_num] = [name,phone]
#2. 딕셔너리 내용 출력
for key,value in student_dict.items():
    print(key," : ",value)

#3. 학번 입력 받아 이름과 연락처 출력
number = input("학번을 입력하시오 : ")
print('이름 : ',student_dict[number][0])
print('연락처 : ',student_dict[number][1])

#4. student_tuple의 마지막 항목으로 학점을 추가한다.
student_dict['202095001'].append(4.5)
student_dict['202095002'].append(3.8)
student_dict['202095003'].append(3.5)

for key,value in student_dict.items() :
    print(key," : ", value)

#5. 학생의 학점 평균을 출력하시오.
print("전체 학생 평균 학점")
sum = 0
for key, value in student_dict.items() : 
    sum = sum + value[2]

print(f"평균 : {(sum/3):.2f}")