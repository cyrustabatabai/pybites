import math
def find_number_pairs(numbers, N=10):

    seen = set()
    result = []

    for i,num in enumerate(numbers): 
        for j in range(i + 1,len(numbers)):
            other_num = numbers[j]
            if math.isclose(num + other_num,N):
                result.append((num,other_num))


    return result




