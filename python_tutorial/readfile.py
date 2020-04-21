###  파일 읽기 ###
'''
open('파일경로/파일명.확장자','모드')

경로 : '\\' 또는 '/'
파일을 일기 모드로 열려면 'r'을
텍스트 파일인 경우에는 't'
'''

f = open("C:\\filetest\\lines.txt",'rt' , encoding = "UTF-8")

lines = f.readlines()

print('lines =>',lines)

'''
출력된 후, 빈 줄이 하나씩 존재
print()는 문자열을 출력할 떄 자동으로 줄 바꿈을 하는데
기존에 lines라는 리스트에 있는 문자열에도
줄 바꿈을 의미하는 값인 '\n' 가 들어있기 때문.

이런식으로 파일을 읽으면 불필요한 기호들 '\n' 포함 기호들이
다 들어온다.
읽어올떄 '\n' 을 빼 달라고 요청하면 표시를 뺄 수 있다.
'''

for line in lines:
    print(line)

'''
lines 리스트에 이는 원소에서 '\n' 기호를 제거함으로써
중복으로 줄 바꿈 되지 않도록 코드를 작성
'''
for line in lines:
    print(line,end="")


#### 파일 쓰기 @###
f = open("C:/filetest/sel_list.txt",'wt')

f.write('삼성전자\n')
f.write('SK하이닉스\n')
f.close
