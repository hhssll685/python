'''
작성일:2023년 11월 15일
적성자:컴퓨터공학부 202095108 한송림
설명:LAB 9-2 : 트위터 메시지 처리의 단어 추츨
띄어쓰기로 문자열을 분리하고,단어의 개수를 찾아라.
'''
text = "There's a reason some people are working to make\
        it harder to vote, especially for people of color. \
        It’s because when we show up, things change."

#띄어쓰기로 문자열을 분리하고,단어의 개수를 찾아라.
#len()=> 길이(개수) : 리스트의 항목 개수 찾는 함수
text2 = text.split()
print(text2)
print('wordl count :',len(text2))


#도진문제 9.1
#회사 이름은 **로 표시
#KT,Samsung,LG,SKT
text = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic \
    Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG \
        U+ Mystic Pink 30%, SKT Mystic Blue not disclosed) '

#모든 문자를 소문자로 변환
low_text = text.lower()
#1.-----------------------------------------------------------------------------
#소문자로 바뀐 단아들을 공백으로 구분한다.
#구분된 단아를 검사한다.(판단)=>단어가 kt 또는 lg 또는 kst 인가?
#검사하는 단어가 화사명이면 **로 바꾼다.
#이니면 그 단어는 그대로 사용한다.
text = ''
for word in low_text.split(' '):
    if word == 'kt' or word == 'samsung' or word == 'lg' or word == 'skt':
        text += '**'
    else:
        text += word +' '
#결과 추력
print('text1 : ',text)
#2.-----------------------------------------------------------------------------
#소문자로 바뀐 딘어들을 공백으로 구분하여 저장한다.
#리스트에 저장된 단어를 검사한다.(판다) => 딘어가 kt또는 samsung또는 lg또는 kst언가?
#검사하는 단어가 회사명이면 **로 바꾼다.
#아니면 그 단어가 회사명이면 **로 바꾸어 리스트에 저장한다.
#분리된 단어들을 합친다.
split_text = low_text.split(' ')
text=''
for word in split_text:
    if word == 'kt' or word == 'samsung' or word == 'lg' or word == 'skt':
        text += word.replace(word,' ** ')
    else:
        text += word + ' '
#출력한다.
print('text2:',''.join(text))