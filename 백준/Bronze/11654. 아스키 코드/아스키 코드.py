#https://seongonion.tistory.com/126 : 아스키코드 관리 포스팅
#ord("str") output: A=65
#chr(int) output: 65=A
#print((ord("Z") + 1 - ord("A")) % 26) 이런식으로 연산 가능
#ascii()란? object(문자열이나 숫자 등 표현 가능한 파이썬 객체)를 유니코드문자 형태로 이스케이프 처리
#try: except:  URL:https://wikidocs.net/30

def func_ascii(N):
    try : print(ord(N))
    except:print(chr(int(N)))

func_ascii(N=input())


