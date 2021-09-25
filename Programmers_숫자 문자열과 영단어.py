def solution(s):
    number = ["zero", "one", "two", "three", "four","five", "six", "seven", "eight", "nine"]
    
    for i in range(len(number)):
        # replace = reaplaceAll in java
        s = s.replace(number[i], str(i))

    return int(s)

print(solution(s="123"))