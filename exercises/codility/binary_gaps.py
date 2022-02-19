# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    if N <= 1:
        return 0

    remaining = N
    binary_gaps = [0]
    gaps_count = 0
    is_first_occurence_of_1 = True

    while remaining >= 1:
        remaining, binary = remaining // 2, remaining % 2
        if binary == 1:
            if not is_first_occurence_of_1:
                binary_gaps.append(gaps_count)
            
            is_first_occurence_of_1 = False
            
            gaps_count = 0
    
        else:
            gaps_count += 1

    return max(binary_gaps)            


