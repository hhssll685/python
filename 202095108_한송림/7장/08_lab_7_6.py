'''
작성일:2023년 11월 1일
적성자:컴퓨터공학부 202095108 한송림
설명:LAB7-6
'''

city_info = [('서울',9765),('부산',3441),('인천',2954),('광주',1501),('대전',1531)]

max_population=0
min_population=999999999999999999
total_population=0

max_city=None
min_city=None

for city in city_info:
    total_population += city[1]
    if city[1] > max_population:
        max_population = city[1]
        max_city = city
    if city[1] < min_population:
        min_population = city[1]
        min_city=city

print("최대인구:{},인구:{}천명".format(max_city[0],max_city[1]))
print("최소인구:{},인구:{}천명".format(min_city[0],min_city[1]))
print("리스트 도시 평균 인구:{}천명",format(total_population/len(city_info)))