# # 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# # 네이버 검색 Open API 예제 - 블로그 검색
# import os
# import sys
# import urllib.request
# import json
# client_id = "twrhEE4LU8HoKxIrMwzM"
# client_secret = "hsPSocfNRK"
# encText = urllib.parse.quote("python")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     result = response_body.decode('utf-8')
# else:
#     print("Error Code:" + rescode)
#
# d1 = json.loads(result)
# # print(d1)
# # print(type(d1))
# # title, description의 내용 출력
# print(d1['items']) # [{},{},{},...]
# for doc in d1['items']:
#     print(doc['title'])
#     print(doc['description'])
#     print('-'*30)

# 번역 접근
# 네이버 Papago NMT API 예제
import os
import sys
import urllib.request
import json
client_id = "NrhObQTo1tZY4TYqD8OQ"
client_secret = "gxstXXfRZ9"
encText = urllib.parse.quote("많이 추워졌어요. 건강 조심하세요")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    result = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
dic = json.loads(result)
# print(dic)
# 번역된 문장만 출력
print(dic['message']['result']['translatedText'])
