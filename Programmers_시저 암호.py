def solution(s, n):
    answer = []
    for char in s:
        if char.isalpha() :
            if 65 <= ord(char) <= 90 :
                if ord(char)+n > 90 :
                    answer.append(chr(ord(char)-26+n))
                else:
                    answer.append(chr(ord(char)+n))
            else :
                if ord(char)+n > 122 :
                    answer.append(chr(ord(char)-26+n))
                else:
                    answer.append(chr(ord(char)+n))
        else:
            answer.append(' ')
    return ''.join(answer)