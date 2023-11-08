'''
작성일:2023년 10월 18일
적성자:컴퓨터공학부 202095108 한송림
설명:입력을 받아 맛있는 과일의 리스트를 만들자

좋아하는 과일 5개를 입력받아 리스트에 저장한다.
과일 이를을 입력하여 해당 과일이 리스트에 있는지 없는지 없는지 찬단한다.

추가 = append() 메소드
찾기 = in 연산자
'''
fruits=[]
for i in range(5):
    fruit_name = input(str(i+1) + "좋아하는 과일의 이름을 입력하시오 :")
    fruits.append(fruit_name)
print("입력한 과일 리스트:",fruits)

#찾기
favo_fruit = input("좋아하는 과일 하나를 입력하세요.:")


#사용자가 입력한 과일이 리스트에 있는지 판단.
#있으면 => 00은 당신이 좋아한는 과일입니다.
#없으면 => 00은 당신이 좋아한는 과일이 아닙니다.

if favo_fruit in fruits:
    print(f'{favo_fruit}은(는) 당신이 좋아하는 과일입니다.')
else:
    print(f'{favo_fruit}은(는) 당신이 좋아한는 과일이 아닙니다.')