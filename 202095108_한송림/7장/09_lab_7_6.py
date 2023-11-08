'''
작성일:2023년 11월 1일
적성자:컴퓨터공학부 202095108 한송림
설명:LAB7-6(2)
'''

city_info = [('서울',9765),('부산',3441),('인천',2954),('광주',1501),('대전',1531)]

max_population=city_info[0][1]
min_population=city_info[0][1]
total_population=0

max_city=city_info[0][0]
min_city=city_info[0][0]

for city, population in city_info:
    total_population += population
    if population > max_population:
        max_population = population
        max_city = city
    if population < min_population:
        min_population = population
        min_city=city

print("최대인구:{},인구:{}천명".format(max_city,max_population))
print("최소인구:{},인구:{}천명".format(min_city,min_population))
print("리스트 도시 평균 인구:{}천명",format(total_population/len(city_info)))