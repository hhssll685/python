'''
작성일:2023년 11월 8일
적성자:컴퓨터공학부 202095108 한송림
설명:LAB8-3
'''

partyA = set(["Park","Kim","Lee"])
partyB = set(["Park","Choi"])
print("2개의 파티에 모두 참석한 사람은 다은과 같습니다.")
print(partyA.intersection(partyB))


partyA = set(["Park", "Kim", "Lee"])
partyB = set(["Park", "Choi"])
common_attendees = ",".join(partyA.union(partyB))
print("파티 A,B에 참석한 사람:"+ common_attendees)


partyA = set(["Park", "Kim", "Lee"])
partyB = set(["Park", "Choi"])
unique_attendees = partyA.symmetric_difference(partyB)
print("파티 A, B 중복없이 참석한 사람: " + ", ".join(unique_attendees))


partyA = set(["Park", "Kim", "Lee"])
partyB = set(["Park", "Choi"])
only_partyA_attendees = partyA.difference(partyB)
print("파티 A에만 참석한 사람: " + ", ".join(only_partyA_attendees))

