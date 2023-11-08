'''
작성일:2023년 11월 8일
적성자:컴퓨터공학부 202095108 한송림
해결 한 사람은 제출하고 수업 끝
'''

student_tuple = [('211101','강이안','010-123-1111'),
                 ('211102','박동민','010-123-2222'),
                 ('211103','김수정','010-123-3333')]

student_dict = {}
#1. 딕셔너리에 추가
for id_num,name,phone in student_tuple:
    print(f"{id_num}:{name}")
    student_dict[id_num] = [name,phone]
#2. 딕셔너리 내용 출력

#3. 학번 입력 받아 이름과 연락처 출력
number = input("학번을 입력하시오 : ")
print(f"{number} 학생은 {student_dict[number][0]}이며 전화번호는 {student_dict[number][1]}입니다.")

