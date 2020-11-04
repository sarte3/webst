# people = {"name": "둘리", "age": "1억살", "addr": "쌍문동"}
# print(people)
# print(type(people))
# print(people['age'])
# # 추가
# people['1004'] = 'yes'
# print(people)
# # 삭제
# del people['age']
# print(people)
# # 수정
# people['1004'] = 'no'
# for i in people:
#     print(i)
# for i in people.items():
#     print(i)
# for i,v in people.items():
#     print(i, v)
# print(people.keys())
# print(people.values())
# 전체 초기화
# people.clear()
# print(people)

# set {}
# a = {2, 5, 3, 5, 8, 2}
# print(a)
# print(type(a))
# b = [1, 2, 3, 4, 1, 2, 3, 4, 2, 1, 3, 4, 5]
# print(b)
# print(set(b))
# # 추가
# a.add(11)
# print(a)
# a.update([13, 5, 17])
# print(a)
# a.remove(2)
# print(a)

# 정규표현식
# ?	 0번 or 1차례 이를테면 colou?r는 "color"와 "colour"를 둘 다 일치시킨다.
# *	0번 이상의 발생을 의미한다. 이를테면 ab*c는 "ac", "abc", "abbc", "abbbc" 등을 일치시킨다.
# + 1번 이상의 발생을 의미한다. 이를테면 ab+c는 "abc", "abbc", "abbbc" 등을 일치시키지만 "ac"는 일치시키지 않는다.
# {n}[6]	정확히 n 번만큼 일치시킨다.
# {min,}[6]	"min"번 이상만큼 일치시킨다.
# {min,max}[6]	적어도 "min"번만큼 일치시키지만 "max"번을 초과하여 일치시키지는 않는다.
# {3}
# {3,}
# {,3}
# | 선택
# [abcdef]
# [a-zA-Z0-9]
# [^ ] 부정
# ^ 시작
# \s 공백
a = '''3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534'''

# 정규식 사용
import re
# re.findall(r '정규식', 문자열)
r1 = re.findall(r'[0-9]', a)
print(r1)
r1 = re.findall(r'[0-9]+', a)
print(r1)
r1 = re.findall(r'[A-Za-z]+', a)
print(r1)
r1 = re.findall(r'[A-SU-Z][a-z]+', a)

print(r1)