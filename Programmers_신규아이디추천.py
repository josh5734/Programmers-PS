
def solution(new_id):
    stack = []
    new_id = list(new_id)[::-1]     # 큐 구조로 저장 
    length = len(new_id)

    for i in range(length):
        next = new_id.pop()
        if next.isupper():
            stack.append(next.lower())
        elif next.isalnum() or next in ['-','_','.']:   # 소문자, 숫자, 허용된 특수문자 가능
            if len(stack) > 0 and stack[-1] == '.' and next == '.': # 연속된 '.' 넣지 않기
                continue
            else:
                stack.append(next)
    
    # 이후 단계별로 조건에 맞게 stack 변경
    if len(stack) > 0 and stack[0] == '.':
        stack.pop(0)
    if len(stack) > 0 and stack[-1] == '.':
        stack.pop()
    
    if len(stack) == 0:
        stack.append('a')
    
    if len(stack) >= 16:
        stack = stack[:15]
        if stack[-1] == '.':
            stack.pop()
    
    if len(stack) <= 2:
        while(len(stack) < 3):
            stack.append(stack[-1])
    
    # 결과 return
    return ''.join(stack)





if __name__ == "__main__":
    new_id = "abcdefghijklmn.p"
    answer = solution(new_id)
    print(answer)
