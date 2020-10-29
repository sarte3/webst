# a = [1, 5, 3, 1, 2, 3, 4, 5]
# print(a)
# print(len(a))
# print(a.count(5))
# # .append(값) - 맨 뒤에 추가
# a.append('seven')
# print(a)
# a.append(['one', 'two', 'three'])
# print(a)
# # a.insert(인덱스,값)
# a.insert(3, '*')
# print(a)
# print(a[9])
# a[3] = '!'
# print(a)
# # 한꺼번에 삭제되는 것이 아니라 첫 번째 값이 삭제됨
# # 리스트의 처음 나타나는 5를 삭제
# a.remove(5)
# print(a)
# a.remove(5)
# print(a)
# # a 리스트의 인덱스 0부터 2번째까지 삭제
# del a[:3]
# print(a)
# # 객체 삭제
# del a
# # print(a)
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = ['zero', 'one', 'two', 'three', 'four', 'five']
# for 변수 in 반복가능객체:
#     내용
# for i in a: # i = 1, 2, ...
#     print(i)
# range(시작,종료(<),증감)
# print(range(1, 10, 1))
# print(list(range(1, 10, 1)))
# print(tuple(range(1, 10, 1)))
# for i in range(6): # 0부터 시작할 때 생략 가능, 1씩 증가 생략 가능
#     print(i, a[i])
# for i in range(len(a)):
#     print(i, a[i])

# for i in range(5): # 종료값, 시작 값 생략시 0, 증감 생략시 1
#     print(i)
# 1~100 숫자 출력
# for i in range(1,101):
#     print(i, end=' ')
# print()
# for i in range(3, 1000, 3):
#     print(i, end=' ')
# print()
# a = [0,1,2,...,100]
# for i in range(101):
#     print(i)
# 컴프리헨션
# a = [i for i in range(101)]
# print(a)
# b = [7,7,...,7]
# for i in range(100):
#     print(7)
# b = [7 for i in range(100)]
# print(b)
# print(len(b))
# c = []
# for i in range(100):
#     c.append(7)
# print(c)
# c = [1,3,5,...,99]
# d = ['good','good',...]
c = [i for i in range(1, 100, 2)]
# d = ['good' for i in range(5)]
# i 값이 사용되지 않아서 의미를 약화시키기 위해 _ 사용
# _ 반복이 5번이지 변수는 의미가 없음을 나타낼 때
d = ['good' for _ in range(5)]
print(c)
print(d)
e = ['good'+str(i) for i in range(5)]
print(e)
# 형변환
# b = '3'
# print(type(b))
# print(int(b), type(int(b)))
