# https://wikidocs.net/book/1
# 파이썬의 모든 것은 객체
# 변수 앞에 아무 것도 없음
# 문자의 끝에 ; 없음
# 따옴표 '', ""
# 문장의 세로줄을 맞춰야 함
# 주석 #
# 실행
# 도움말 ctrl+click
# a = 3
# print(a)
# a = 'machinelearnnning'
# print(a)
# a = 3.1
# print(a)
# a = True
# # print("a의 값은 =",a,"그럼 이만")
# print("a의 값은 =",a,"그럼 이만",sep='*',end='!')
# print("새로운 줄")
# print('-'*30)
# a = 30
# b = 5
# print(a,b)
# print(type(a)) #<class 'int'>
# a='machine'
# print(type(a)) #<class 'str'>
# # 형변환
# print('b의 값은 = '+str(b))
# a=7
# b=10
# print(a,b)
# temp=a
# a=b
# b=temp
# print(a,b)
# a,b=b,a
# print(a,b)
# a,b,c,d=3,0,True,'5'
# print(a,b,c,d)
# print(type(a),type(b),type(c),type(d))
# print(bool(a))
# print(bool(b))
# d=int(d)
# print(type(d))
# print(a,d)
#
# # 산술연산자
# print("a+d=",a+d)
# print("a-d=",a-d)
# print("a*d=",a*d)
# print("a/d=",a/d)
# print("a//d=",a//d) # 몫
# print("a%d=",a%d) # 나머지
# print("a**d=",a**d) #
#
# # 관계연산자
# print(a>d)
# print(a<=d)
# print(a==d)
# print(a!=d)

# age=21
# b1=age<10
# b2=age>20
# print(b1,b2)
# print(10<=age<=30)

# 문자열
# 문자열 : '..',"..",'''...''',"""..."""
# a = '문자열 표현방"법" @123!'
# print(a)
# a = '문자열 표현방\'법\' @123!'
# print(a)
# # '''...''' 여러줄 문자
# a='''
# IDLE로 파이썬 프로그램 작성하기
# 명령 프롬프트 창에서 파이썬 프로그램 실행하기
# 추천 에디터
# 비주얼 스튜디오 코드
# 파이참
# '''
# print(a)
# a='python'
# b='machine'
# print(a+b)
# print(a*5)

# 문자열 인덱싱 : 문자열중에서 특정 데이터를 획득,[]
# [인덱스],
# [시작인덱스:끝인덱스] 시작인덱스<=x<끝인덱스
# a='0123456789'
# print(a)
# print(a[3]) # 정방향
# print(a[-3]) # 역방향
# print(a[3:7])
# print(a[3:-3])
# print(a[:-3])
# print(a[3:])
# print(a[:])
# a = 'pithon'
# # print(a[1])
# # a[1]='y' # 문자열은 그 요소값을 변경 안됨
# print(a[:1]+'y'+a[2:])
# 포멧팅
# a = 10
# b = 20
# c = 'green'
# print(a, b, c)
# print('[%s + %s = %s %%]'%(a,b,c))
# # 2.대 버전에서 쓰는 포맷팅
# # %s 문자열 %d 정수 %f 실수 %o 8진수 %x 16진수
# print('[%d + %d = %s]'%(a,b,c))
# #3.대 버전에서 쓰는 포맷팅
# print("{} + {} = {}".format(a,b,c))

# 문자열 함수
a = '12312412412532526646245'
print(a.count('1'))
print(a.count('0'))
print(a.find('0')) # 없으면 -1
print(a.find('5')) # 중복되면 가장 앞에 있는 위치가 뜸
# print(a.index('0')) index는 없으면 오류 처리
print(a.index('5'))

