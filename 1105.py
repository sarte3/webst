import json
j1 = '{"ip": "8.8.8.8"}'
j2 = '''{
   "Accept-Language": "en-US,en;q=0.8",
   "Host": "headers.jsontest.com",
   "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "food": true,
   "ab": null
}'''
# print(type(j1))
# print(type(j2))
#
# # loads 문자열을 딕셔너리로
# d1 = json.loads(j1)
# print(type(d1))
# print(d1)
# print(d1['ip'])

d2 = json.loads(j2)
print(d2)
print(type(d2))

j3 = json.dumps(d2)
print(type(j3))
print(j3)
