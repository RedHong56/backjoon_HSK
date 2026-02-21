def solution(cipher, code):
    answer = ''
    for i in cipher[code-1::code]:
        answer += i
    return answer