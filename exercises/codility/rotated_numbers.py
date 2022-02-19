def solution(A, K):
    
    rotated = list(A)
    mod = K % len(A)

    for index, element in enumerate(A):

        if ((index + mod) < len(rotated)):
           rotated[index + mod] = element

        else:
            rotated[(index + mod) - len(rotated)] = element

    return rotated

