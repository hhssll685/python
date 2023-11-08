'''
작성일:2023년 10월 18일
적성자:컴퓨터공학부 202095108 한송림
설명:
'''

population = ["Seoul",9765,"Busan",3441,"Incheon",2954]

print('서울 인구:',population[1])
print('인천 인구:',population[-1])

cities=population[0::2]
print('도시 리스트:',cities)
pops = population[1::2]
print('인구의 합:',sum(pops))