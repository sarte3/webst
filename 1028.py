# a = "  blue  red  green "
# # 문자열 길이 len()
# print(len(a))
# print("["+a+"]")
# print("["+a.lstrip()+"]") # 왼쪽 공백 삭제
# print("["+a.rstrip()+"]") # 오른쪽 공백 삭제
# print("["+a.strip()+"]") # 양쪽 공백 삭제
# print("["+a+"]")
# # .replace('찾는 문자열','바꿀 문자열') 문자열치환
# print(a.replace(' ', ''))
# print(a.upper(), a.lower())
# a = "one-two-three four-five six"
# print(type(a))
# # .split(문자열) : 문자열 기준으로 자르기
# print(a.split('-'))
# print(a.split(' '))
# print(type(a.split(' '))) # <class 'list'>
# b = a.split(' ')
# print(b)
# # '기호'.join(리스트)
# print('!'.join(b))
# print(type('!'.join(b)))
# line = input()
# # input() enter치기 전까지 값을 입력받기
# print(line, type(line))
# print(line.split())
# collection
# [] list : 인덱스는 0부터 시작
# () 튜플
# {} 딕셔너리, set
# <> not used
# a = [1, 56, 'blue', ['one', 'two', 'three'], 111, True]
# print(a, len(a))
# print(a[0])
# print(a[0:3])
# print(a[3:])
# print(a[5])
# print(a[3:5]) # 끝 인덱스는 포함되지 않음
# print('-'*30)
# print(a[3])
# print(a[3][1])
# # ------
b = ['토마토', '감', '포도']
print(b[1])
b[2] = '캠벨'
print(b)
# 리스트 추가 .append(값)
b.append('샤인머스킷')
print(b)
# sorted(대상) : 정렬
print(sorted(b))
a = [3 ,78, 100, 55, 4]
print('합계 : ', sum(a))
print('평균 : ', sum(a)/len(a))
# print(reversed(b))
# print(list(reversed(b)))
# dir(a) a객체에 사용할 수 있는 함수
print(dir(a))
# 컴프리핸션