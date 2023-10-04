'''
작성일:2023년10월4일
작성자:컴퓨터공학부 202095108 한송림
설명:반복을 재어하는 break,continue
    교제 137 패이지
'''
word = input("단어를 입력하세요:")

print("::break1::")
for i in word:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        break
    else:
        print(i, end='')

print()

print("::break2::")
for i in word:
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        break
    else:
        print(i, end='')

print()

print("::continue::")
for i in word:
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        continue
    print(i, end='')
